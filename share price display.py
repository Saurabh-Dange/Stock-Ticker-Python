from bs4 import BeautifulSoup
import requests
import notify2
import time

count = 0

flag = True

while flag:
    response = requests.get(
        'http://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS') #Enter url of your desired stock from moneycontrol website
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    tags = soup.find_all('span', id="Bse_Prc_tick")
    notify2.init("stock price")
    n = notify2.Notification(None)
    n.set_timeout(1)
    print(tags)
    for tag in tags:
        div = tag.strong
        for c in div.children:
            count += 1
            n.update("TCS price" + str(count), c)
            n.show()
            flag = False
            time.sleep(10)
            flag = True


