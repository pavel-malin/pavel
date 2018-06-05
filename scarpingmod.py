from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re
import random
import HTTPError
import json




random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)(?!:).)*$"))
def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url is: "+historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserLink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
        return addressList
    links = getLinks("/wiki/Python_(programming_language)")
    while(len(links) > 0):
        for link in links:
            print("---------------------")
            historyIPs = getHistoryIPs(link.attrs["href"])
            for historyIP in historyIPs:
                print(historyIP)
                newLinks = links[random.randint(0, len(links)-1)].attrs["href"]
                links = getLinks(newLinks)


                def getCountry(ipAddress):
                    try:
                        response = urlopen("http://freegeiop/net/json/"+ipAddresses).read().decode('utf-8')
                    except HTTPError:
                        return None
                    responseJson = json.loads(response)
                    return responseJson.get("Country_language")
                while(len(links)>0):
                    for link in links:
                        print("------------")
                        historyIPs = getHistoryIPs(link.attrs["href"])
                        for historyIP in historyIPs:
                            country = getCountry(historyIP)
                            if country is not None:
                                print(historyIP+"is from "+country)
                                newLink = link[random.randint(0,len(links)-1)].attrs["href"]
                                links = getLinks(newLink)
