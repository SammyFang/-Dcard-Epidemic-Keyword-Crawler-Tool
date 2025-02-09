import requests
import bs4
import re
import os
import time
import datetime
import sqlite3
import cloudscraper
import json
import random

def lineNotifyMessage(token, message,isNotificationDisabled = False):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {
        'message': message,
        'notificationDisabled': isNotificationDisabled
    }
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=payload)
    
    print("網路活動狀態碼：",r.status_code)
    time.sleep(1)
    
def spider_dcard_ndhu(token):
    scraper = cloudscraper.create_scraper()
    data = scraper.get("https://www.dcard.tw/service/api/v2/forums/ndhu/posts")
    info =data.json()
    for item in info:
        store_details = {}
        store_details['Title:'] = item['title']
        store_details["Link:"] = item['id']
        idn1 = int(item['id'])
        sql = "SELECT * FROM articles WHERE idp = '%d'" % (idn1)
        c.execute(sql)
        result = c.fetchone()
        
        if result != None:
            print('====暫無新文章====')
            time.sleep(random.randint(121,496))
            continue
        
        if("快篩"in item['title'] or
           "線上教學"in item['title'] or
           "遠距"in item['title'] or
           "防疫"in item['title'] or
           "足跡"in item['title'] or
           "免疫"in item['title'] or
           "傳播鏈"in item['title'] or
           "疫苗"in item['title'] or
           "普篩"in item['title'] or
           "本土"in item['title'] or
           "確診"in item['title'] ):
            
            print("Title = ",item['title']+"\n"+"Link = "+"https://www.dcard.tw/f/ndhu/p/"+str(item['id'])+"\n")
            msg = '\n'
            msg += '\n[標題]：%s' % item['title']
            msg += '\n[網址]：https://www.dcard.tw/f/ndhu/p/%s' % item['id']
            msg += "\n*** 使用Dcard NDHU爬蟲工具 ***\n*** Dev by 方方 *** v0.0.3 ***"
            lineNotifyMessage(token=token, message=msg)
            
            idn = item['id']
            tit = str(item['title'])
            
            sql = "INSERT INTO 'articles' ('idp','title') VALUES ('%d','%s')" % (idn,tit)
            c.execute(sql)
            conn.commit()
print("============================================================\n*** 歡迎使用Dcard NDHU爬蟲工具 v0.0.3 請依照使用說明操作 ***\n*** Dev by 方方 ***僅供開發使用不負相關責任並保留所有權利***\n============================================================")            
token = " Use your token"
while (1):
    conn = sqlite3.connect('./Dcard.db')
    c = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS 'articles'(\
            'idp' INTEGER NOT NULL,\
            'title' TEXT NOT NULL\
        )"
    c.execute(sql)
    conn.commit()
    spider_dcard_ndhu(token)
    conn.close()
