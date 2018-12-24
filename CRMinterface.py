import requests
import  json 
import uuid
import time

session = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjYyODhhM2FhNDgyNTVhZjk4MzA4N2IwMDlmNjJmOWRhIiwidHlwIjoiSldUIn0.eyJuYmYiOjE1NDUzOTMyMDEsImV4cCI6MTU0NTQ3OTYwMSwiaXNzIjoibnVsbCIsImF1ZCI6WyJudWxsL3Jlc291cmNlcyIsImNybSIsImRpbmd0YWxrIiwiaHIiXSwiY2xpZW50X2lkIjoiZGluZ3RhbGsiLCJzdWIiOiJhMWMyZTJlYS1kOWI0LTRjMTEtYjdhZi1kMDg4YThlNDFmM2MiLCJhdXRoX3RpbWUiOjE1NDUzOTMyMDEsImlkcCI6ImxvY2FsIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZSI6IuayiOaWjOWwj-Wwj-WPtyIsIm5hbWUiOiLmsojmlozlsI_lsI_lj7ciLCJkaW5ndGFsa191c2VyaWQiOiI0ODY2NjU4ZjBlZDU0NWJiYjcwNmFiOTZmNzRiYWQwOCIsImRlcGFydG1lbnRzIjoiMjIsMjMiLCJhbGxkZXBhcnRtZW50cyI6IjIyLDI0LDI1LDIzLDI2LDI3Iiwic2NvcGUiOlsib3BlbmlkIiwicHJvZmlsZSIsImNybSIsImRpbmd0YWxrIiwiaHIiXSwiYW1yIjpbImRpbmd0YWxrX2NvZGUiXX0.FkWMCVklZMfNjoepRE0uXPvh3pwzHOvjD9YYJWwanR4nq4yjb0Z7dXA6X0UY5Cgd84GWc-Gcr8D5ZbleiFwdq1UEmQLcS-HAFlbIeWureHfcBVCPq1onZZJKBWnHMKBb2-hl3I18O1BF3I_VpTSdHqKvDVbyjMeUEdovMgxCg7G_y1gmlXBCdYZOTNMIq6dT-v6zROlfQVZ7SWgV4WssetCM1Y0VIWtXkt3K9Y6Pvotg8SDV62HKsjAqWA1QngoZnWyyzHBEzNCdyITi5yTI-xT5lBzmYuMjj3y7OhUXW6OZDAlKJDRK1W6-M1jy8hjLlICltU21iVNjFOPeg6GShA'
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
while i <= 1:
  time.sleep(1)
  requestid = str(uuid.uuid1())
  apiurl = url + 'api/Customer/create'
  headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
  payload ={
    "name": "小小号有限公司"+str(i),
    "shortName": "小小科技"+str(i),
    "city": "浙江省",
    "state": "杭州市",
    "departmentId":27,
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
