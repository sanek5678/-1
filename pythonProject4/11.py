import requests
from bs4 import BeautifulSoup
url = "https://prokosmos.site/zvezdy/10-krupnejshih-zvyozd-vo-vselennoj/?ysclid=lsih1medc3256983532"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
response = requests.get(url, headers=header)
#html = response.text
soup = BeautifulSoup(response.content, 'html.parser')
conteiner = soup.find("div", {"class":"wp-block-heading"})
elements = soup.find_all("h2")
string = "Топ звезд самых больших: \n"
with open(file="1.txt", mode="w", encoding='utf8')as file:
    for element in elements:
        string += element.get_text() +'\n'
        #file.write("Топ звезд самых больших:\n")
        #file.write(str(elemet.get_text()))
    file.write(str(string))