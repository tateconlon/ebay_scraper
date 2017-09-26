import json
import requests
search_term = "E5-2620"
keyFile = open("APIkey.txt", "r")
key = keyFile.readline()
search_term = "poster"

url = ("http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=findItemsByKeywords\
&sortOrder=PricePlusShippingLowest\
&buyerPostalCode=92128\
&SERVICE-VERSION=1.13.0\
&SECURITY-APPNAME=" + key +
"&RESPONSE-DATA-FORMAT=JSON\
&REST-PAYLOAD\
&itemFilter(0).name=Condition\
&itemFilter(0).value=New\
&itemFilter(1).name=MaxPrice\
&itemFilter(1).value=500.0\
&itemFilter(1).paramName=Currency\
&itemFilter(1).paramValue=USD\
&keywords=" + search_term)

#print(url)

apiResult = requests.get(url)
parseDoc = apiResult.json()
for item in (parseDoc["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
	title = item["title"][0]
	condition = item["condition"][0]["conditionDisplayName"][0]
	price = item["sellingStatus"][0]["convertedCurrentPrice"][0]["__value__"]
	print("{0} {1} {2}".format(title, price, condition))
