import schedule
import time

import requests
from bs4 import BeautifulSoup
from lxml import etree

import telegram
import asyncio

bot = telegram.Bot(token='6396401126:AAFC0BNwC8yMQPum_o7rEIhGkuJOi_Oos7w')
chat_id = 305295334

asyncio.run(bot.sendMessage(chat_id=chat_id, text="Starting Bot..."))

def GetXPathData(dom, string):
	return dom.xpath(string)[0].text

def GetUSDCData(dataset):
	for coin in dataset.xpath_dict.keys():
		text = coin + " " +GetXPathData(dataset.dom, dataset.xpath_dict[coin]) + " USDC Issued"
		asyncio.run(bot.sendMessage(chat_id = chat_id, text = text))

class USDC_Cool():
	def __init__(self):
		self.url = 'https://usdc.cool/'
		self.res = requests.get(self.url)
		self.res.raise_for_status()

		self.soup = BeautifulSoup(self.res.content, "html.parser")
		self.dom = etree.HTML(str(self.soup))

		self.xpath_dict = {
			'TOTAL': '//*[@id="__next"]/div/div/main/div/div[3]/div[3]/div[3]/div[1]/span[2]',
			'ETH': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[1]/a/div[3]/div[1]/span[2]',
			'SOL': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[2]/a/div[3]/div[1]/span[2]',
			'ARB': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[3]/a/div[3]/div[1]/span[2]',
			'TRX': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[4]/a/div[3]/div[1]/span[2]',
			'AVAX': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[5]/a/div[3]/div[1]/span[2]',
			'BASE': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[6]/a/div[3]/div[1]/span[2]',
			'MATIC': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[7]/a/div[3]/div[1]/span[2]',
			'ALGO': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[8]/a/div[3]/div[1]/span[2]',
			'OP': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[9]/a/div[3]/div[1]/span[2]',
			'NOBLE': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[10]/a/div[3]/div[1]/span[2]',
			'XLM': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[11]/a/div[3]/div[1]/span[2]',
			'FLOW': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[12]/a/div[3]/div[1]/span[2]',
			'HBAR': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[13]/a/div[3]/div[1]/span[2]',
			'NEAR': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[14]/a/div[3]/div[1]/span[2]',
			'DOT': '//*[@id="__next"]/div/div/main/div/div[3]/div[1]/div/ul/li[15]/a/div[3]/div[1]/span[2]'
		}


dataset = USDC_Cool()
schedule.every(2).hours.do(GetUSDCData, dataset)

while True:
	schedule.run_pending()
	time.sleep(1)