from pprint import pprint
from bs4 import BeautifulSoup
import requests
def amazon(p):
	a = "https://www.amazon.in/s/ref=nb_sb_noss?url=search&field-keywords="+p

		# add header
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
	r = requests.get(a, headers=headers)
	
	print(r);
	soup = BeautifulSoup(r.content, 'html.parser')
	title= soup.find_all('a', attrs={'class':'a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal'})

	# lists for name, links to the product page and price
	titles  = []
	links = []
	prices = []

	for i,tag in enumerate(title):
		t = tag.get('title',None)
		titles.append(t)
		l = tag.get('href',None)
		links.append(l)


	price = soup.find_all('span', attrs={'class':'a-size-base a-color-price s-price a-text-bold'})
	for i in price:
		prices.append(i.contents[1])
	amazall = dict(zip(titles,prices))
	# print(amazall)
	return (amazall)
