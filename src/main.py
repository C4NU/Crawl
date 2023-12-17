import schedule
import time
####################
import crawl
####################
import telegram
import asyncio

from dotenv import load_dotenv
import os

value_data = dict()

def get_xpath_data(dom, string):
	return dom.xpath(string)[0].text

def human_format(num):
	num = float('{:.3g}'.format(num))
	magnitude = 0
	while abs(num) >= 1000:
		magnitude += 1
		num /= 1000.0
	return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

def calc_difference(value_old, value_new):
	if value_old is not None:
			change = value_new - value_old
			rate = (change / value_old) * 100 if value_old != 0 else 0
			return f'{rate:.2f}'
	else:
		return '0.00%'

async def send_data():
	text = time.strftime('%Y-%m-%d %H:%M:%S\n')
	for coin in dataset.xpath_dict.keys():
		try:
			value_data[coin][0] = value_data[coin][1]
		except:
			value_data[coin] = [0,0]

		value = get_xpath_data(dataset.dom, dataset.xpath_dict[coin])
		value = value.replace(',', '')
		value_data[coin][1] = int(value)

		difference = calc_difference(value_data[coin][0], value_data[coin][1])

		value_format = human_format(value_data[coin][1])
		text = text + (coin + " | " + value_format + " USDC Issued, " + difference + "% \n")

	await bot.sendMessage(chat_id=chat_id, text=text)

async def task(interval_time, func):
	while True:
		await func()
		await asyncio.sleep(interval_time * 3600)

if __name__ == '__main__':
	load_dotenv()

	dataset = crawl.USDC_Cool()
	token = os.environ.get('token')
	chat_id = os.environ.get('chat_id_personal')

	bot = telegram.Bot(token=token)

	interval_time = 2

	loop = asyncio.get_event_loop()
	loop.run_until_complete(task(interval_time, send_data))