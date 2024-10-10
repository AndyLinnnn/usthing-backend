
import requests
from bs4 import BeautifulSoup

def web(restaurant=None):
	url = "https://cso.ust.hk/special-opening-hours"
	page = requests.get(url)

	data = BeautifulSoup(page.content, "html.parser")

	dataFetchOdd = data.find_all("tr", class_="odd")
	dataFetchEven = data.find_all("tr", class_="even")

	dataFetch = dataFetchOdd + dataFetchEven

	dataFetchResult = []

	for i in dataFetch:
		dataFetchResult.append(i.text.strip())
	
	if restaurant == None:
		return dataFetchResult
