import requests
import  json 
import uuid
import time

session = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjU4YjVkNTExYTRlYzViNjU4YjVjZWE1MzU4MDMzMDA1IiwidHlwIjoiSldUIn0.eyJuYmYiOjE1NDUwMTU4NjUsImV4cCI6MTU0NTEwMjI2NSwiaXNzIjoibnVsbCIsImF1ZCI6WyJudWxsL3Jlc291cmNlcyIsImNybSIsImRpbmd0YWxrIiwiaHIiXSwiY2xpZW50X2lkIjoiZGluZ3RhbGsiLCJzdWIiOiJiZGYyMWMyYi1jNjk1LTQ2ZWUtYjZlOS1lMTgzYzhkNzM4ZDAiLCJhdXRoX3RpbWUiOjE1NDUwMTU4NjUsImlkcCI6ImxvY2FsIiwibmFtZSI6IuayiOaWjCIsImRpbmd0YWxrX3VzZXJpZCI6ImE4OGI5MjFhZjY2MDQzZDE4MGE5ZmVhMTRjMjE1YTg1Iiwic2NvcGUiOlsib3BlbmlkIiwicHJvZmlsZSIsImNybSIsImRpbmd0YWxrIiwiaHIiXSwiYW1yIjpbImRpbmd0YWxrX2NvZGUiXX0.aEnHSmQm9U0zdmpSuN7evpMmyEI4gYR41TOI7xS7N8Bqdd36-huIskImr9s_UeZypVxHHBDKvwQs5LrD-wnbDqbV0HpAFcM4yIkcKbL_K5Fnz2_xihe5JOpDTPkgY_xTZ7cWE6H5ndZUge_LiCVBS67wdWkP2UMrIQx7C8QQCLD_MLXYLKLdBh49inHweRwJrHJnoy7n8DvSHrqbpF6ujNTrCLmnzOCw70F7EJnDMRP0vWJXvRndrFKgS_KxMojDlkfW6PIARDi9jFsqA7h04ImIOHJ5Z4gLye2ujGd5bZddx_14uoYCReW79pHkVFZ7C7Owb_0IFHFRdqqasZWYrw'
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


# i=1
# while i <= 5:
#   time.sleep(1)
#   requestid = str(uuid.uuid1())
#   apiurl = url + 'api/Customer/create'
#   headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
#   payload ={
#     "name": "小小号科技有限公司"+str(i),
#     "shortName": "小小号科技"+str(i),
#     "city": "浙江省",
#     "state": "杭州市",
#     "customerProspectId": 3,
#     "customerTypeId": 2,
#     "labelIds":[9],
#     "customerKind":2,
#     "synopsis":"111"
#   }
#   r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
#   print(r.status_code)
#   i=i+1


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



#创建项目
i=1
while i <= 5:
  time.sleep(1)
  apiurl = url + 'api/Project/create'
  requestid = str(uuid.uuid1())
  headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
  payload ={
      "projectName": "阿里投资项目"+str(i),
      "customerId": "38AF8FE6-18AA-4289-86A8-63D5D9025767",
      "status": "63",
      "departmentId": "17",
      "projectType": "1",
      "investmentProject": {
      "amount": 100,
      "estimate": 100,
      "conditions": "11",
      "commitment": "22",
      "newSituation": "33"
    }
  }
  r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
  print(r.status_code)
  i=i+1





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
