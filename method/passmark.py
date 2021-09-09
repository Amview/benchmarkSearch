from bs4 import BeautifulSoup

from method import RRequest

def passmarkData(url):
    text = RRequest.request(url)
    soup = BeautifulSoup(text,'lxml')
    li = soup.find("ul", {"class": "chartlist"}).find_all("li")
    dict = {}
    for item in li:
        name = item.find("span", {"class": "prdname"}).text
        score = item.find("span", {"class": "count"}).text
        # print(name + "--" + score)
        dict2 = {name: score}
        dict.update(dict2)
    return dict
