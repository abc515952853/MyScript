import requests
import  json 
import uuid

session = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjBjNjM2MDJiNTMxOWU5Y2ZiMmY3Yzg2MGQyMzJiNjNiIiwidHlwIjoiSldUIn0.eyJuYmYiOjE1NDQwNjMxMTQsImV4cCI6MTU0NDE0OTUxNCwiaXNzIjoibnVsbCIsImF1ZCI6WyJudWxsL3Jlc291cmNlcyIsImNybSIsImRpbmd0YWxrIiwiaHIiXSwiY2xpZW50X2lkIjoiZGluZ3RhbGsiLCJzdWIiOiJjMWY2Nzc3MC04MTA0LTRhOGQtOTFmMy0zZTcwMjU0N2EzNjUiLCJhdXRoX3RpbWUiOjE1NDQwNjMxMTQsImlkcCI6ImxvY2FsIiwibmFtZSI6IuayiOaWjCIsImRpbmd0YWxrX3VzZXJpZCI6ImE4OGI5MjFhZjY2MDQzZDE4MGE5ZmVhMTRjMjE1YTg1Iiwic2NvcGUiOlsib3BlbmlkIiwicHJvZmlsZSIsImNybSIsImRpbmd0YWxrIiwiaHIiXSwiYW1yIjpbImRpbmd0YWxrX2NvZGUiXX0.Z2eE-vQ13KN5JTUD9E6yQ8pdMdS_HuSHH_xUAIU3TGH4N-jV9r7WJ1JgfwA87fwd2JzKZX9ZqR7PRx1CygvuTDmuxGLR04m1nb4u59Bx4w64kXqKeN5gkV5GmzP2tAslo3nnuHNtSo_zLqyjcyMRPaiVEEPN3XIw-Sqw5r44Ub3TeBz_glcgZ8QmoGETj1fsH5FgK0A5nQW-zkhVLHtjZPNipX0XVpjVM4kvxQ_Bfg_-wNYy8yIqrCJQLv_kk4zu0H6iA-zjs-vDEcJGen9QOkbRo1eTn3vs7T3JGoBKNs9UXb7a46ek6gKUubiBfelldSVbtXAvUhw9iUtdU7Erww'
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

apiurl = url + 'api/Customer/create'
headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
payload ={
  "name": "杭州千之海科技有限公司",
  "shortName": "千之海",
  "street": "33",
  "city": "浙江省",
  "state": "杭州市",
  "customerProspectId": 4,
  "customerTypeId": 3
}
r = requests.post(url=apiurl, headers = headers,data = json.dumps(payload))
print(r.status_code)


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