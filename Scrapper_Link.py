import bs4, requests
import re

res = requests.get('https://swarajyamag.com/world/who-says-b1617-is-now-variant-of-concern-what-do-we-know-so-far-about-double-mutant-covid-variant')
soup = bs4.BeautifulSoup(res.content, 'html5lib')

file = open("Content.txt",'w',encoding = 'utf-8')

file.write((soup.title.string+"\n"))
cont = soup.find_all('p')
cont[1:-1]
for link in cont:
    print(link.getText())
    file.write(str(link.getText()+"\n"))
file.close()
