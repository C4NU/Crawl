import requests
from bs4 import BeautifulSoup
from lxml import etree

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