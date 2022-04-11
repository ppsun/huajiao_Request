# -*- coding:utf-8 -*-


import requests
import time
import random
import hashlib


userid = ""


time = str(int(time.time()))
rand = str(random.random())
platform = "ios"
version = "8.2.3"

def getGuid(userid):

    g = "platform=" + platform + "rand=" + rand + "time=" + time + "userid=" + userid + "version=" + version + "eac63e66d8c4a6f0303f00bc76d0217c"

    md5 = hashlib.md5()
    md5.update(g.encode('utf-8'))
    guid = md5.hexdigest()

    return guid





def sendReq(url, method, **data):

    for key, value in data.items():
        if key == "params":
            params = value
        if key == "files":
            files = value
        if key == "headers":
            headers = value

    if method == 'get':
        res = requests.get(url=url, headers=headers, params=params)
    elif method == 'post':
        res = requests.post(url=url, headers=headers, params=params, files=files)

    resData = res.json()

    if resData.get("errno") == 0:
        return resData
    else:
        print(resData.get("errmsg"))


#登录guid
guid = getGuid("0")
#print(guid)

headers = {
    'Host': "passport.huajiao.com",
    'User-Agent': 'living/8.2.3 (iPhone; iOS 15.3.1; Scale/3.00)',
    # 'Content-Type': 'multipart/form-data; boundary=Boundary+8D7C241AF7DBE5D8',
    'Accept': '*/*',
    'Accept-Language': 'zh-Hans-CN;q=1',
    'Accept-Encoding': 'gzip',
    'Connection': 'keep-alive'
    }

params = {
        'userid': "0",
        'time': time,
        'rand': rand,
        'platform': platform,
        'version': version,
        'guid': guid
    }
files = {
        "agreement_version": (None, '1'),
        "mbcode": (None, "+86"),
        "mobile": (None, "+8615811431882"),
        "password": (None, "47ec2dd791e31e2ef2076caf64ed9b3d"),
        "lat": (None, "40.08299888940655"),
        "lng": (None, "116.5228648730338")
    }

loginRes = sendReq("https://passport.huajiao.com/user/login", "post", headers=headers, params=params, files=files)
print(loginRes)

userid = loginRes.get("data").get("uid")
token = loginRes.get("data").get("token")
cookie = "token=" + token
#print(type(cookie))

f1 = open('/user_file.txt', 'w')
f1.write(userid)
f1.close()

f2 = open('/user_file.txt')
#print(f2.readline())









