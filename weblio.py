#-*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup as bs
import re

class Weblio(object):
	title = "None"
	translation = "None"
	others = "None"
	prediction_all = {}

	def __init__(self, word):
		URL = (
			"http://ejje.weblio.jp/content/")
		URL += word
		r = requests.get(URL)
		soup = bs(r.text, "html.parser")
		self.get_title(soup)
		self.get_translation(soup)
		if self.title == "None":
			self.get_others(soup)
			if self.others != "予測候補なし":
				self.get_prediction_all(soup)

	def get_title(self,soup):
		self.title = soup.find(id="h1Query")
		if self.title != None:
			self.title = self.title.string
			toha = soup.find(id="h1Suffix")
			if toha != None:
				toha = toha.string
				self.title += toha
		else:
			self.title = "None"

	def get_translation(self, soup):
		self.translation = soup.find("td", class_="content-explanation")
		if self.translation != None:
			self.translation = self.translation.string
		else:
			self.translation = "None"

	def get_others(self, soup):
		self.others = soup.find("p", class_="nrCntSgHl")
		if self.others != None:
			self.others = self.others.string
		else:
			self.others = "予測候補なし"

	def get_prediction_all(self, soup):
		self.prediction_all = {}
		prediction = soup.find_all(class_="nrCntSgT")
		preList = []
		if prediction != []:
			for pre in prediction:
				pre = pre.find("a").string
				preList.append(pre)
		preTrans = soup.find_all(class_="nrCntSgB")
		preTransNew = []
		if preTrans != []:
			for pre in preTrans:
				pre = pre.string.replace("\n", "")
				preTransNew.append(pre)
		for (a, b) in zip(preList, preTransNew):
			self.prediction_all[a] = b

################others method##########################
def get_example(word):
	r = requests.get("http://ejje.weblio.jp/sentence/content/" + word)
	soup = bs(r.text, "html.parser")
	example = []
	sentences = soup.find_all(class_="qotC", limit=10)
	for s in sentences:
		example.append(s.text.replace("例文帳に追加", " =>", 1).split(" - ")[0])
	return example


#weblio = Weblio(input(">"))
#print(weblio.example)
