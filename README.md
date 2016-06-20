# python-spider
这是我的python爬虫笔记
Beautifulsoup 使用 </br>
<textarea><tag> = tag<> </textarea></br>
 BeautifulSoup 的 a=soup.find_all() a=soup.selector() 返回的是列表 a[0] 返回tag 再用tag.attrs 返回字典 
字典包含 tag的属性
tag.get("src")  获取属性 </br>
tag>.get_text() 获取tag文本</br>
soup.find_all("div",class_="") </br>
soup.select(xpath,Css selector) Css格式中的div和>中的空格一定不能少 不然无法识别 爬去失败 （>  div  >  div ）  </br>
两者不能混用</br>

tag.stripped_strings 获取标签下所有字标签的内容</br>
list(tag.stripped_strings) 将其列表化</br>
<textarea>a = soup.select("img[width="200"]")</textarea></br>
</br>

<h2>图片下载到本地的方法 </h2></br>
url = http://wanzao2.b0.upaiyun.com/system/pictures/36202611/original/1464746641_813x2395.png    #图片的url</br>
respone = urllib2.urlopen(url)  #下载图片</br>
a= response.read()  #读取图片信息</br>
f=open("name.png","wb") #创建空白 图片</br>
f.write(a) #将图片的信写入 图片中</br>
