import requests
import  json 
import uuid

session = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjBjNjM2MDJiNTMxOWU5Y2ZiMmY3Yzg2MGQyMzJiNjNiIiwidHlwIjoiSldUIn0.eyJuYmYiOjE1NDQxNDk0MjgsImV4cCI6MTU0NDIzNTgyOCwiaXNzIjoibnVsbCIsImF1ZCI6WyJudWxsL3Jlc291cmNlcyIsImNybSIsImRpbmd0YWxrIiwiaHIiXSwiY2xpZW50X2lkIjoiZGluZ3RhbGsiLCJzdWIiOiJiNzI2YTk1Mi04Mzc2LTRhN2ItODNlNC1kYWE1ZmFlNWE2YjkiLCJhdXRoX3RpbWUiOjE1NDQxNDk0MjgsImlkcCI6ImxvY2FsIiwibmFtZSI6IuW8oOi2hSIsImRpbmd0YWxrX3VzZXJpZCI6ImI0ZjcwYWEyYTcxNzQzNDI5NzMyZjAzZmU4MTQ2MDYyIiwic2NvcGUiOlsib3BlbmlkIiwicHJvZmlsZSIsImNybSIsImRpbmd0YWxrIiwiaHIiXSwiYW1yIjpbImRpbmd0YWxrX2NvZGUiXX0.ud3J28KxS7EnOmi_ufC-kJhES94_N5v1zFDbYoyDmZmEyK1vDbtk9BlBrty1q_89RzBNpPCTrgiBUvz_JS3bz5o2k-0lftXlzmHBJrsctLm6HV7jvB9D31jMtJZcNqJ0izo6jjavvmi-mt3QBfSoExwt5vacmjhV02cR6ofxaZcO_nDuwTnzmikKj6Ie-0p8yV7CSDZPLcVTCLcalNY8T5c8Zi2lO_NSmYA6fe465Ob1mx09Ppht-N0ehv7W32-OWxSPMkVQEozzEQNh-tAmi0BcgvOinx63z1fQbmvylDpsTYfBZbeeKJ8wVgjLXh3OyMakXMaVAPc8jCBcRjMPVw'
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
i=2
while i <= 50:
  requestid = str(uuid.uuid1())
  apiurl = url + 'api/Customer/create'
  headers = {'Content-Type': "application/json",'Authorization':session,"x-requestid":requestid}
  payload ={
    "name": "阿超科技有限公司"+str(i),
    "shortName": "阿超科技"+str(i),
    "street": "33",
    "city": "浙江省",
    "state": "杭州市",
    "customerProspectId": 4,
    "customerTypeId": 3
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