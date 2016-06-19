# python-spider
这是我的python爬虫笔记
Beautifulsoup 使用 </br>
1. <tag>.attrs  BeautifulSoup 的 a=soup.find_all() a=soup.selector() 返回的是列表 a[0] 返回<tag> 再用<tag>.attrs 返回字典 
字典包含 <tag>的属性
<tag>.get("src")  获取属性 </br>
<tag>.get_text() 获取<tag>文本
