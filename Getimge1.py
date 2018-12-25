import glob
import os
import time
import random

def chosePic(number):
    pic_list = glob.glob('*.jpg')
    up_pic = random.sample(pic_list, number)
    return up_pic

def upPic(pic_list):
    up_url = '127.0.0.1/api/User?sort=tourDating'
    re = []
    for pic in pic_list:
        f = open(u'%s' % pic, 'rb')
        files = {'file':[os.path.split(pic)[-1], f.read(), 'application/octet-stream']}
        f.close()
        req = requests.post(up_url, files=files)
        server_path = req.json()[0]
        re.append(server_path)
    path = ','.join(re)
    return path

if __name__ == "__main__":
    up_pic=chosePic(random.randint(1,3))
    # path=upPic(up_pic)
    print(up_pic)