import requests
import sys
from bs4 import BeautifulSoup


def flipkart(text):
	
	r = requests.get('https://www.flipkart.com/search?q='+text) 
	
	print(r);

	content = r.content.decode(encoding='UTF-8')
	soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")
	reviews = soup.find_all('div', {"class": "_3wU53n"})
	titles = []
	for i in reviews:
		titles.append(i.contents[0])
	link = soup.find_all('a',attrs={'class':'_1UoZlX'})
	links=[]
	for i,tag in enumerate(link):
	    print (i)
	    ans = tag.get('href',None)
	    links.append(ans)
	    print ("\n")
	price = soup.find_all('div',{'class':"_1vC4OE _2rQ-NK"})
	prices=[]
	for i in price:
		prices.append(i.text)
	flipall = dict(zip(titles,prices))
	# print (flipall)
	return (flipall)
