# -*- coding: UTF-8 -*-
#practice
# import urllib.request as request
# import ssl
# ssl._create_default_https_context=ssl._create_unverified_context
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") #取得台灣大學網站的原始碼（HTML CSS JS)
#     print(data)
#Q1:
#為了網路連線，載入網路模組
import urllib.request as request
#為了JSON檔案，載入json模組
import json
#解決urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed問題
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
#打開連線的網址並將資料讀取，可將網址打開觀察資料
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)#利用JSON模組處理JSON資料格式
#將景點名稱列表抓取出來並寫入另一個創建的檔案中
siteList=data["result"]["results"]#此class is list
# print(type(siteList[0]["file"]))#從list選取字典by[index], 從字典選取value by["key"]
#打開一個資料with open("檔案名稱", "mode", encoding="utf-8"因為資料有中文)
with open("data.csv", "w", encoding="utf-8") as file:
# print(siteList)
    for site in siteList:
    #檔案寫入景點名稱並換行
        file.write(site["stitle"]+",")
        file.write(site["address"][5:8]+",")#substring a string
        file.write(site["longitude"]+",")
        file.write(site["latitude"]+",")
        #先將片網址內容轉換為小寫
        #將string用split分開，split會把separator刪掉，所以再把separator加回去
        #取出file list，使用spilt以jpg為separator
        modContent=site["file"].lower()
        imgUrl=modContent.split("jpg")
        #從list取得第0個元素並將"jpg"加回來，"\n"為換行
        file.write(imgUrl[0]+"jpg"+"\n")


