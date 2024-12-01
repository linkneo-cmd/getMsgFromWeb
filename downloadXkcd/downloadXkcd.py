# downloadXkcd.py

import os
import requests
import bs4
import time

url = "https://xkcd.com"  # starting url
# 创建存放漫画的文件夹，兼容文件夹已经存在的情况
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

# 计时30s，可以自行随意更改下载时间
start_time = time.time()
timeout = 30

# 第一页的prev链接是#，所以循环终止条件是url的结尾是#
while not url.endswith('#'):

    # 超过timeout时间自动退出循环
    if time.time() - start_time > timeout:
        print(f"Timeout reached. Exiting.")
        break
    # 获取每个页面的 HTML 文本信息
    print(f"Downloading page {url}")
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Find the URL of the comic image
    comic_elem = soup.select("#comic img")
    if comic_elem == []:
        print("Could not find comic image.")
    else:
        comic_url = 'https:' + comic_elem[0].get('src')

        # Download the image
        print(f"Downloading image {comic_url}")
        res = requests.get(comic_url)
        res.raise_for_status()

        # 将下载的图片保存在./xkcd文件夹中
        with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as imgFile:
            imgFile.write(res.content)

        # 查找所有rel 属性为"prev"的a 元素，获取其href属性的值
        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prev_link.get('href')

print('Done.')