# -*- coding: utf-8 -*-
# 写入图片
import os
import urllib2
from bs4 import BeautifulSoup
# info =[]
# with open('baozou.html','r') as wb_data:
#     soup = BeautifulSoup(wb_data,'html.parser')
#
#     names = soup.select('.article-author-name')
#     contents =soup.select(".article-title")
#     imgs = soup.select('div.article-body > div.article-content > a > img')
#     dates =soup.select(' div.article-meta.user-item-wrap.clearfix > div.article-meta-body > div > div.pull-right > span')


    # print date[1].get_text()
    # #print img[0]
    # print img[0].get("src")
    # # article-36564441 > div.article-body > div.article-content > a > img
    # for i in name:
    #     print i.get_text()
    # for c in content:
    #     print c.get_text()
#
# for name , date ,content,img in zip(names,dates,contents,imgs):
#     url_data={
#         "name" :name.get_text(),
#         "date" :date.get_text(),
#         "content" : content.get_text(),
#         "img"  :img.get("src")
#     }
#     info.append(url_data)

urls=["http://baozoumanhua.com/users/7634849/articles/page/{}?order=latest".format(str(i)) for i in range(1,20)]
info=[]


def download(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response,"html.parser")
    return soup

def html_parser(soup):
    try:
        print  "网页下载 并写入中"
        names = soup.select('.article-author-name')
        contents = soup.select(".article-title")
        imgs = soup.select('div > div.article-body > div.article-content > a > img')
        dates = soup.select(' div.article-meta.user-item-wrap.clearfix > div.article-meta-body > div > div.pull-right > span')
        # article-36238530 > div.article-body > div.article-content > a > img
        for name, date, content, img in zip(names, dates, contents, imgs):
            url_data = {
                "name": name.get_text(),
                "date": date.get_text(),
                "content": content.get_text(),
                "img": img.get("data-original-image-url")
            }
            info.append(url_data)

        return info
    except:
        print "下载失败"
i=0
j=0

for i in urls:
    j=j+1
    soups=download(i)
    print "下载网页---------- 第 %s页"%j
    text =  html_parser(soups)


for a in info:
    i=i+1
    print "保存第%s张图片--------"%i

    f = open("暴走漫画/%s.png"%i,"wb")
    response=urllib2.urlopen(a["img"])
    content =response.read()
    f.write(content)
    f.close()
