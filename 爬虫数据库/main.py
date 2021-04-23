import requests
import pymysql
from lxml import etree
import re
import time
import random
#
url="https://movie.douban.com/top250?start="
headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54"
}
#
urls=[]
jianjies=[]
daoyans=[]
titles=[]
shijians=[]
stars=[]
amounts=[]

for i in range(0,25,25):
    url=url+str(i)
    responses=requests.get(url=url,headers=headers).text
    with open('xiangqing.html','w',encoding='utf-8') as f:
        f.write(responses)
    # 获取url
    result = re.findall('<a href="(.*?)" class="">', responses)
    for j in result:
        urls.append(j)
    time.sleep(random.random()*10)

print(urls)

for url_0 in urls:
    responses1 = requests.get(url=url_0, headers=headers).text
    with open('xiangqing.html', 'w', encoding='utf-8') as f:
        f.write(responses1)
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.parse('xiangqing.html', parser)

    # 简介
    rb = tree.xpath('//span[@ property="v:summary"]//text()')
    x = str(rb[0])
    "".join(x.split())
    jianjies.append(x)
    # 导演
    rb1 = tree.xpath('//div[@ id="info"]//span[1]//text()')
    daoyans.append(rb1[2])
    # title
    rb2 = tree.xpath('//span[@ property="v:itemreviewed"]//text()')
    titles.append(rb2[0])
    # time
    rb3 = tree.xpath('//span[@ property="v:initialReleaseDate"]//text()')
    shijians.append(rb3[0][:4])
    # star
    rb4 = tree.xpath('//strong[@ class="ll rating_num"]/text()')
    stars.append(rb4[0])
    # amount
    rb5 = tree.xpath('//span[@ property="v:votes"]/text()')
    amounts.append(rb5[0])
    time.sleep(random.random() * 10)

db = pymysql.connect(host="localhost", user="root", password="root", database="qg_works")
# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()
for i in range(25):
    sql="INSERT INTO `qg_works`.`movie` (`title`,`director`,`time`,`star`,`amount`,`Introduction`) VALUES ( '%s','%s','%s','%s','%s','%s')" % (titles[i],daoyans[i],shijians[i],stars[i],amounts[i],jianjies[i])
# #sql = "INSERT INTO `user` (`movie_id`, `name`, movie_content, actor, `date`, country, types,rate, com_count)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (movie_id, name, movie_content, actor, date, country, types,rate, com_count)
# sql = "INSERT INTO `qg_works`.`movie` (`title`,`director`,`time`,`star`,`amount`,`Introduction`) VALUES ( '%s','%s','2002-4-12','%s','%s','%s')" % (h1,h2,h4,h5,h6)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
db.close()






# url_0='https://movie.douban.com/subject/1296141/'
#
# responses1 = requests.get(url=url_0, headers=headers).text
# with open('xiangqing.html', 'w', encoding='utf-8') as f:
#     f.write(responses1)
# parser = etree.HTMLParser(encoding='utf-8')
# tree = etree.parse('xiangqing.html', parser)
#
# # 简介
# rb = tree.xpath('//span[@ property="v:summary"]//text()')
# x = str(rb[0])
# "".join(x.split())
# jianjies.append(x)
# # 导演
# rb1 = tree.xpath('//div[@ id="info"]//span[1]//text()')
# daoyans.append(rb1[2])
# # title
# rb2 = tree.xpath('//span[@ property="v:itemreviewed"]//text()')
# titles.append(rb2[0])
# # time
# rb3 = tree.xpath('//span[@ property="v:initialReleaseDate"]//text()')
# shijians.append(rb3[0][:4])
# # star
# rb4 = tree.xpath('//strong[@ class="ll rating_num"]/text()')
# stars.append(rb4[0])
# # amount
# rb5 = tree.xpath('//span[@ property="v:votes"]/text()')
# amounts.append(rb5[0])
# time.sleep(random.random() * 10)
#
# print(titles)
# print(daoyans)
# print(shijians)
# print(stars)
# print(amounts)
# print(jianjies)
#
# db = pymysql.connect(host="localhost", user="root", password="root", database="qg_works")
# # 使用cursor()方法创建一个游标对象cursor
# cursor = db.cursor()
# for i in range(1):
#     sql="INSERT INTO `qg_works`.`movie` (`title`,`director`,`time`,`star`,`amount`,`Introduction`) VALUES ( '%s','%s','%s','%s','%s','%s')" % (titles[i],daoyans[i],shijians[i],stars[i],amounts[i],jianjies[i])
# # #sql = "INSERT INTO `user` (`movie_id`, `name`, movie_content, actor, `date`, country, types,rate, com_count)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (movie_id, name, movie_content, actor, date, country, types,rate, com_count)
# # sql = "INSERT INTO `qg_works`.`movie` (`title`,`director`,`time`,`star`,`amount`,`Introduction`) VALUES ( '%s','%s','2002-4-12','%s','%s','%s')" % (h1,h2,h4,h5,h6)
#     try:
#         # 执行sql语句
#         cursor.execute(sql)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         # 如果发生错误则回滚
#         db.rollback()
# db.close()
