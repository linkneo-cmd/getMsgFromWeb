import sys
import requests
import bs4
import webbrowser

print("Searching ...")  # display text while downlading the search result page

# https://pypi.org/search/?q=也可以替换成其他搜索的 url 地址
res = requests.get("https://pypi.org/search/?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()
# print(res.text)
# 写入文件中，便于分析哪些 html 是自己需要的
playFile = open('pypi.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'lxml')
# 跳转链接存在于 class 为 package-snippet 的 a 标签中
linkElems = soup.select('.package-snippet')
# 少于 5 条就打开所有的，否则取前五条打开
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    # 拼接完整的 url 地址，循环打开 tab 页
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opeing', urlToOpen)
    webbrowser.open(urlToOpen)