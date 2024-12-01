import requests
import bs4

# res = requests.get("https://nostarch.com")
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(noStarchSoup))

# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# elems = exampleSoup.select('#author')
# print(elems[0])
# print(elems[0].get_text())

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('p')
for elem in elems:
    print(elem.get_text())