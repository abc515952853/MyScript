import threading
import time
import requests
from datetime import datetime
from xlrd import xldate_as_tuple

import xlrd
import xlwt

import random

# 获取毫秒级时间
def get_time_ms():
    ct = time.time()    # 时间戳
    local_time = time.localtime(ct) # 本地化时间
    cart_time_strftime = time.strftime("%Y-%m-%d %H:%M:%S", local_time)  # 格式化时间
    cart_time_strftime_ms = (ct - int(ct)) * 1000
    ms = "%s.%03d" % (cart_time_strftime, cart_time_strftime_ms) # 拼接，获取毫秒级时间
    return ms

#获取excl数据
def get_excl_data():
    readbook = xlrd.open_workbook(r'testcase.xlsx')
    sheet = readbook.sheet_by_name('UserName')

    row = sheet.row_values(0)
    rowNum  = sheet.nrows
    colNum = sheet.ncols 
    
    cls = []
    curRowNo = 1
    while has_next(rowNum,curRowNo):
        s = {}  
        col = sheet.row_values(curRowNo)  
        i = colNum  
        for x in range(i):
            s[row[x]] = conversion_cell(sheet,curRowNo,x,col[x])
        cls.append(s)  
        curRowNo += 1
    return cls

def has_next(rownum,curRowNo):  
    if rownum == 0 or rownum <= curRowNo :  
        return False  
    else:  
        return True 

def conversion_cell(sheet,curRowNo,curColNo,cell):
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

def chose_data(data,num):
    return data[num]['phone']
    

# 定义请求函数
def login(phone):
    # session = requests.session()
    # url = "https://www.cnblogs.com/xuxiongbing/p/9475772.html"
    # try:
    #     jmt_request = session.get(url)
    #     status_code = jmt_request.status_code
    #     return status_code
    # except Exception as e:
    #     return str(e)   
    print(phone)


if __name__ == '__main__':
    phonedata = get_excl_data()

    threads = []
    for jk in range(1,1000):
        phone = chose_data(phonedata,random.randint(1,15))  #随机获取一个手机号
        s = threading.Thread(target=login,args=(phone,))    # 把请求函数加入多线程中去
        threads.append(s)    

    for t in threads:
        t.setDaemon(True)           # 把多线程设置为守护线程
        t.start()             # 开始执行多线程
        print (('%s 执行时间为 %s') % (t,get_time_ms()))     # 输出执行时间
    t.join()       # 阻塞主线程执行
    print("all over %s" % get_time_ms())
    exit()