import requests
import  json 
import uuid
import time

session = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1MjAxNmY3ZmYzOTJiYTMwNmE4NjNjZjAyMzFkNWRkIiwidHlwIjoiSldUIn0.eyJuYmYiOjE1NDc3MTk3MDksImV4cCI6MTU0NzgwNjEwOSwiaXNzIjoibnVsbCIsImF1ZCI6WyJudWxsL3Jlc291cmNlcyIsImNybSIsImRpbmd0YWxrIiwiZmlsZSIsImhyIiwicHJvY2Vzc2VzIl0sImNsaWVudF9pZCI6ImRpbmd0YWxrIiwic3ViIjoiYmRmMjFjMmItYzY5NS00NmVlLWI2ZTktZTE4M2M4ZDczOGQwIiwiYXV0aF90aW1lIjoxNTQ3NzE5NzA5LCJpZHAiOiJsb2NhbCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWUiOiLmsojmlowiLCJuYW1lIjoi5rKI5paMIiwiZGluZ3RhbGtfdXNlcmlkIjoiYTg4YjkyMWFmNjYwNDNkMTgwYTlmZWExNGMyMTVhODUiLCJkZXBhcnRtZW50cyI6IjM1IiwiYWxsZGVwYXJ0bWVudHMiOiIzNSIsImlzU2VuaW9yIjoiVHJ1ZSIsInNjb3BlIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJjcm0iLCJkaW5ndGFsayIsImZpbGUiLCJociIsInByb2Nlc3NlcyJdLCJhbXIiOlsiZGluZ3RhbGtfY29kZSJdfQ.TmXfVAtwvcss96qqBipHOO1pen2Nv58rt7FB_VXelGRs5P31EEeiaV3zYrik2EjY6Wp9cJw1qFQ8Ao6x2dXBTi3KKjqkfwLC5DUrsm-VaUW6U3EmSXhmEvYh9TBD8hMyRThuO6D_H2djdQTZqI0svu0ZpI4wuJOzqPKdQI7GQ7zd7dY7UzG3UT8YtZus-p_fB4hJ3J-xP_aLZUCU34K35p6s9yWS31V8OF7rSbDynOQPe_tpaONnGlLS_IToBV6DXqkQ9oBh_gz0sMGYmbJPHgufSiSK1965rYaKnkErnwC05nL-3r0V9xEA1PURrMkxdNqQTcqLVyoP2cxMa67j1g'
requestid = str(uuid.uuid1())
url = 'http://api.syzb.qianjifang.com.cn/'

# apiurl = url + 'api/Contact'
# headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
# payload = {
#     "name": "沈斌斌斌99",
#     "phone": "18011110099",
#     "labelIds": [317323129]
# }
# r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
# print(r.status_code)


i=1
while i <= 5:
  time.sleep(1)
  requestid = str(uuid.uuid1())
  apiurl = url + 'api/Customer/create'
  headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
  payload ={
    "name": "保理二组测试客户"+str(i),
    "shortName": "测试客户"+str(i),
    "city": "浙江省",
    "state": "杭州市",
    "departmentId":16,
    "labelIds":[41],
    "customerKind":2,
  }
  r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
  print(r.status_code)
  i=i+1


# apiurl = url + 'api/Customer/AddSchedule'
# headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
# payload ={
#     'beginTime':"2018-12-30 17:35",
#     'endTime':"2018-12-30 18:35",
#     'minutes':1440,
#     'summary':"1321",
#     'visitTypeId':1,
# }
# r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
# print(r.status_code)



# #创建项目
# i=1
# while i <= 1:
#   time.sleep(1)
#   apiurl = url + 'api/Project/create'
#   requestid = str(uuid.uuid1())
#   headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
#   payload ={
#       "projectName": "撒的撒"+str(i),
#       "customerId": "38AF8FE6-18AA-4289-86A8-63D5D9025767",
#       "status": "63",
#       "departmentId": "17",
#       "projectType": "1",
#       "investmentProject": {
#       "amount": 100,
#       "estimate": 100,
#       "conditions": "11",
#       "commitment": "22",
#       "newSituation": "33"
#     }
#   }
#   r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
#   print(r.status_code)
#   i=i+1





# #项目列表
# apiurl = url + 'api/Project/38AF8FE6-18AA-4289-86A8-63D5D9025767/all'
# headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
# r = requests.get(url=apiurl, headers = headers)
# print(r.status_code)

# #修改项目名称
# apiurl = url + 'api/Project/7546BA47-9E89-4DF2-B84D-38CFAE68BD49/ProjectName'
# headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
# payload ={
#   "projectName": "项目2号"
# }
# r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
# print(r.status_code)


# #修改项目状态
# apiurl = url + 'api/Project/7546BA47-9E89-4DF2-B84D-38CFAE68BD49/Status'
# headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
# payload ={
#   "status": 64
# }
# r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
# print(r.status_code)

# #修改投资情况
# apiurl = url + 'api/Project/38AF8FE6-18AA-4289-86A8-63D5D9025767/Status'
# headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
# payload ={
#   "amount": 1000
# }
# r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
# print(r.status_code)
