#!/user/bin/env python
#coding=utf-8
import requests
import datetime
import time
import threading

from xlrd import xldate_as_tuple

import xlrd
import xlwt

import random
import  json 

import uuid

class read_excl():
    #获取excl数据
    def get_excl_data(self):
        readbook = xlrd.open_workbook(r'testcase.xlsx')
        sheet = readbook.sheet_by_name('UserName')

        row = sheet.row_values(0)
        rowNum  = sheet.nrows
        colNum = sheet.ncols 
        
        cls = []
        curRowNo = 1
        while self.has_next(rowNum,curRowNo):
            s = {}  
            col = sheet.row_values(curRowNo)  
            i = colNum  
            for x in range(i):
                s[row[x]] = self.conversion_cell(sheet,curRowNo,x,col[x])
            cls.append(s)  
            curRowNo += 1
        return cls

    def has_next(self,rownum,curRowNo):  
        if rownum == 0 or rownum <= curRowNo :  
            return False  
        else:  
            return True 

    def conversion_cell(self,sheet,curRowNo,curColNo,cell):
        #判断python读取的返回类型  0 --empty,1 --string, 2 --number(都是浮点), 3 --date, 4 --boolean, 5 --error  
        if sheet.cell(curRowNo,curColNo).ctype == 2:
                no = int(cell)          
        elif sheet.cell(curRowNo,curColNo).ctype == 3:
            # 转成datetime对象
            date = datetime(*xldate_as_tuple(cell, 0))
            no = date.strftime('%Y-%m-%d')
        else:
                no = cell
        return no

    def chose_data(self,data,num):
        return data[num]['phone']


class url_request():
    times = []
    error = []

    def login(self,phone):
        myreq=url_request()

        url = 'http://api.syzb.qianjifang.com.cn/api/Project/create'
        headers = {'Content-Type': 'application/json', 'x-requestid': str(uuid.uuid1()), 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjYyODhhM2FhNDgyNTVhZjk4MzA4N2IwMDlmNjJmOWRhIiwidHlwIjoiSldUIn0.eyJuYmYiOjE1NDU3MDI0NDksImV4cCI6MTU0NTc4ODg0OSwiaXNzIjoibnVsbCIsImF1ZCI6WyJudWxsL3Jlc291cmNlcyIsImNybSIsImRpbmd0YWxrIiwiaHIiXSwiY2xpZW50X2lkIjoiZGluZ3RhbGsiLCJzdWIiOiJiZGYyMWMyYi1jNjk1LTQ2ZWUtYjZlOS1lMTgzYzhkNzM4ZDAiLCJhdXRoX3RpbWUiOjE1NDU3MDI0NDksImlkcCI6ImxvY2FsIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZSI6IuayiOaWjCIsIm5hbWUiOiLmsojmlowiLCJkaW5ndGFsa191c2VyaWQiOiJhODhiOTIxYWY2NjA0M2QxODBhOWZlYTE0YzIxNWE4NSIsImRlcGFydG1lbnRzIjoiMSIsImFsbGRlcGFydG1lbnRzIjoiMSIsInNjb3BlIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJjcm0iLCJkaW5ndGFsayIsImhyIl0sImFtciI6WyJkaW5ndGFsa19jb2RlIl19.G7YRn5DNJKm2334lButnPauc_bq07i9LDP3b1S6ztsuDHh5Kx53b50t-vrqrtg2AVc28ebD8077UVqeaXVvPh09ca2gZmw_P5zuasa0SfqyxwOy3aJ20Ab7xmGzN1uCXpznLfe3JxbnWJORpCNCpb0LyZeSGILkzKYmLO0KSs7lhot30tyL0F16ak1jJHCUulwmI24eRDL4vtEC9HTLJPUEPQ0KRfyfYYBiFdQxm3--ZoXy3M1OWuOPaxUTmOMJ4YilNOZWoBVK4yg0I9c79flY2RrGSizkundevaKx_65tlFm0A5oV4fIjgMyhh6cfTP-5CfX5G7cx-n8SwLKe5ww'}
        payload = {'departmentId': '17', 'customerId': '38AF8FE6-18AA-4289-86A8-63D5D9025767', 'projectName': '投行项目1号', 'status': 63, 'investmentProject': {'conditions': 'aaa', 'commitment': 'aaa', 'amount': 1, 'estimate': 1, 'newSituation': 'aaa'}}
        r = requests.post(url=url,data = json.dumps(payload),headers = headers)

        ResponseTime=float(r.elapsed.microseconds)/1000 #获取响应时间，单位ms
        myreq.times.append(ResponseTime) #将响应时间写入数组
        if r.status_code <200 or  r.status_code > 300:
            print(r.status_code,r.text)
            myreq.error.append("0")


if __name__=='__main__':
    myphone = read_excl()
    phonedata = myphone.get_excl_data()

    myreq=url_request()
    threads = []
    starttime = datetime.datetime.now()
    print ("开始时间： %s" %starttime )
    print ("running...")
    nub = 1000#设置并发线程数
    ThinkTime = 0#设置思考时间

    for i in range(1, nub+1): 
        phone = myphone.chose_data(phonedata,random.randint(1,2000))#随机获取一个手机号
        t = threading.Thread(target=myreq.login, args=(phone,))
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime) 
        # print ("thread %s" %t) #打印线程)
        t.setDaemon(True)
        t.start()
    t.join()

    endtime = datetime.datetime.now()
    print ("结束时间： %s" %endtime)
    time.sleep(3)
    AverageTime = "{:.3f}".format(float(sum(myreq.times))/float(len(myreq.times))) #计算数组的平均值，保留3位小数
    print ("平均响应时间: %s ms" %AverageTime) #打印平均响应时间)
    usetime = str(endtime - starttime)
    hour = usetime.split(':').pop(0)
    minute = usetime.split(':').pop(1)
    second = usetime.split(':').pop(2)
    totaltime = float(hour)*60*60 + float(minute)*60 + float(second) #计算总的时间+请求时间
    print ("并发数:%s" %nub) #打印并发数
    print ("总共消耗的时间 %s s" %(totaltime-float(nub*ThinkTime))) #打印总共消耗的时间
    print ("错误请求数 %s" %myreq.error.count("0")) #打印错误请求数