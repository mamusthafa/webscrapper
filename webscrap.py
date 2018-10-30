from bs4 import BeautifulSoup
import requests
import bs4
#insert the link which you want to scrap from
data = requests.get('https://www.flipkart.com/search?q=coffee&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
soup = bs4.BeautifulSoup(data.text,'html')
#inside braket mention the class name
for i in soup.select('._2cLu-l'):
    #print the desired item/tag
    print(i.text)




