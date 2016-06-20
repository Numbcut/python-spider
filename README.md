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
