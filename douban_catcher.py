# 豆瓣相册爬虫
# author:zsw
# date:2022/3/13

from bs4 import BeautifulSoup
import requests
import os
import time

headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 Edg/99.0.4844.51"
    }


class DoubanPhotosCatcher:

    #明星相册页面
    __url = ""

    #保存抓取的图片链接
    __photoUrls = []

    def __init__(self, url) -> None:
        self.__url = url

    def run(self):
        r = requests.get(self.__url, headers=headers)
        html = r.text

        # todo 分页
        soup = BeautifulSoup(html, 'html.parser')
        #总页数
        pageNum = soup.select('.paginator a')[-2].text
        #每页的数量
        pageSize = 30
        index = 0
        while index < int(pageNum):
            print('抓取第' + str(index+1) + "页")
            url = self.__url + '?type=C&start=' + str(index * pageSize) + '&sortby=like&size=a&subtype=a'
            index += 1
            self.parse(html, url, index)
    
    def parse(self, html, url, index):
        r = requests.get(url, headers=headers)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
  
        #抓取图片url
        imgTags = soup.select('#wrapper #content .cover img')
        for tag in imgTags:
            self.__photoUrls.append(tag['src'])

        self.download(index)
        
    def download(self, index):
        name = self.__url.split("/")[4]
        os.makedirs("D:\\celebrity\\" + name, exist_ok=True)

        size = len(self.__photoUrls)

        i = 0
        while i < size:
            print("no." + str(index) + "-" + str(i) + "is downing...")
            r = requests.get(self.__photoUrls[i])
            with open("D:\\celebrity\\" + name + "\\" + str(index) + "-" + str(i) + ".jpg", 'wb') as f:
                f.write(r.content)

            i += 1
            if i % 5 == 0:
                time.sleep(1)

    


if __name__ == '__main__':
    url = "https://movie.douban.com/celebrity/1044702/photos/"
    catcher = DoubanPhotosCatcher(url)
    catcher.run()

