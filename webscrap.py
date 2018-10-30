from bs4 import BeautifulSoup
import requests
import bs4
data = requests.get('https://www.flipkart.com/search?q=coffee&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
soup = bs4.BeautifulSoup(data.text,'html')
for i in soup.select('._2cLu-l'):
    print(i.text)




