from bs4 import BeautifulSoup
import requests
url = "https://finance.naver.com/sise/sise_quant.nhn"

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html,'html.parser')

data = soup.select(".type_2 tr .number")
for i in range(0,len(data)):
    print(data[i].get_text().strip(), end = " ")
    if i%10 == 9:
        print('\n------------')
