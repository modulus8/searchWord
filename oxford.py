#-*- coding:utf-8 -*-

import requests as rq
from bs4 import BeautifulSoup as bs

class Oxford(object):
	title = "None"
	pronounce = "None"
	mp3 = "None"
	headers = {
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
		'Upgrade-Insecure-Requests':'1',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate',
		'Accept-Language':'ja,en-US;q=0.8,en;q=0.6',
		'Connection':'keep-alive',
		'Cookie':'localisation=JP; __gads=ID=630dd1872028cbfa:T=1492868378:S=ALNI_MaL7A9USuFhNmErBvIPkvcxz1svpA; oup-cookie=true; __qca=P0-776163548-1492868381763; JSESSIONID=9C1A89991B6BAA790C9E436140A2A16A; _ga=GA1.2.166593092.1492868379; _gid=GA1.2.1845099481.1499518413; _gat=1; dictionary=english',
		'Host':'www.oxfordlearnersdictionaries.com',
		'Referer':'http://www.oxfordlearnersdictionaries.com/definition/english/apple?q=apple',
	}
	

	def __init__(self, word):
		oxford = rq.get(
			"http://www.oxfordlearnersdictionaries.com/definition/english/" + word, headers=self.headers, allow_redirects=True)
		soup = bs(oxford.text, "html.parser")
		self.get_title(soup)
		self.get_pronouce(soup)
		self.get_mp3(soup)
	
	def get_title(self, soup):
		self.title = soup.find("h2", class_="h")
		if self.title != None:
			self.title = self.title.text
		else:
			self.title = "None"
	
	def get_pronouce(self, soup):
		self.pronounce = soup.find("div", class_="pron-gs ei-g")
		if self.pronounce != None:
			self.pronounce = self.pronounce.find_all(class_="phon")
			self.pronounce = [p.text for p in self.pronounce]
		else:
			self.pronounce = "None"
	
	def get_mp3(self, soup):
		self.mp3 = soup.find("div", class_="pron-gs ei-g")
		if self.mp3 != None:
			self.mp3 = self.mp3.find_all(class_="sound audio_play_button pron-us icon-audio")[0]
			self.mp3 = self.mp3.get("data-src-mp3")
		else:
			self.mp3 = "None"



