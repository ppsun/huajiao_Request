# -*- coding:utf-8 -*-


import requests
import time
import random
import hashlib


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


#登录guid
guid = getGuid("0")


class sendRequest:

    def __init__(self, method, url):
        self.method = method
        self.url = url


    def getRes(self,**kwargs):
        for key, value in kwargs.items():
            if key == "params":
                self.params = value
            elif key == "headers":
                self.headers = value
            elif key == "data":
                self.data = value

        if self.method == "get":
            res = requests.get(url=self.url, params=self.params, header=self.headers)
        elif self.method == "post":
            res = requests.post(url=self.url,params=self.params,headers=self.headers,files=self.data)

        resData = res.json()
        return resData



if __name__ == '__main__':
    headers = {
        'Host': 'passport.huajiao.com',
        'User-Agent': 'living/8.2.3 (iPhone; iOS 15.3.1; Scale/3.00)',
        # 'Content-Type': 'multipart/form-data; boundary=Boundary+8D7C241AF7DBE5D8',
        # 'Referer': 'https://passport.huajiao.com/',
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

    data = {
        "agreement_version": (None, '1'),
        "mbcode": (None, "+86"),
        "mobile": (None, "+8615811431882"),
        "password": (None, "47ec2dd791e31e2ef2076caf64ed9b3d"),
        "lat": (None, "40.08299888940655"),
        "lng": (None, "116.5228648730338")
    }

    hujiaoLogin = sendRequest("post","https://passport.huajiao.com/user/login")
    resData1=hujiaoLogin.getRes(headers=headers,params=params,data=data)
    print(resData1)


