# 从web获取信息
## request_get.py
下载《罗密欧与朱丽叶》并打印前 250 个字符
## bs4_get.py
使用 BeautifulSoup4 获取 example.html 中的 html 内容并筛选处理
## searchpypi.py
打开  https://pypi.org/  搜索到的前 5 个包的信息，并自动在 tab 页中打开

使用前提：
pip install beautifulsoup4
pip install requests
pip install lxml

使用方法：
python searchpypi.py 包名(python3 searchpypi.py 包名)
![alt text](image.png)
自动在浏览器中打开搜索结果的前五个 tab 页详情
![alt text](image-1.png)
结果和自行在搜索框搜索结果一致
![alt text](image-2.png)

扩展：程序改编后同样适用于其他网站

## downloadXkcd.py
下载 xkcd 网站的所有漫画，持续下载 30s 后自动停止
使用前提：
pip install beautifulsoup4
pip install requests
pip install lxml

使用方法：
python downloadXkcd.py(python3 downloadXkcd.py)
![alt text](image-3.png)
下载图片保存在此处
![alt text](image-4.png)

扩展：顺着网站的所有链接本分整个网站，复制整个论坛的所有信息，复制一个在线商店中所有产品目录等
### TODO：
1、怎么监控当前内存资源消耗情况
2、怎么并行下载，让下载更多内容时处理的更快？