import schedule
import time
####################
import crawl
####################
import telegram
import asyncio

from dotenv import load_dotenv
import os

load_dotenv()

dataset = crawl.USDC_Cool()

def get_xpath_data(dom, string):
	return dom.xpath(string)[0].text

def human_format(num):
	num = float('{:.3g}'.format(num))
	magnitude = 0
	while abs(num) >= 1000:
		magnitude += 1
		num /= 1000.0
	return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

async def main():
	token = os.environ.get('token')
	chat_id = os.environ.get('chat_id_personal')

	bot = telegram.Bot(token=token)

	text = time.strftime('%Y-%m-%d %H:%M:%S\n')
	for coin in dataset.xpath_dict.keys():
		value = get_xpath_data(dataset.dom, dataset.xpath_dict[coin])
		value = value.replace(',', '')
		print(value)
		value = int(value)
		value = human_format(value)
		text = text + (coin + " | " + value + " USDC Issued\n")
	await bot.sendMessage(chat_id=chat_id, text=text)

asyncio.run(main())