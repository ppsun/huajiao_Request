# -*- coding:utf-8 -*-


import login

#请求feed接口guid
guidFeed = login.getGuid("0")

headers = {
    'Host': "live.huajiao.com",
    'User-Agent': 'living/8.2.3 (iPhone; iOS 15.3.1; Scale/3.00)',
    # 'Content-Type': 'multipart/form-data; boundary=Boundary+8D7C241AF7DBE5D8',
    'Accept': '*/*',
    'Accept-Language': 'zh-Hans-CN;q=1',
    'Accept-Encoding': 'gzip',
    'Connection': 'keep-alive',
    'Cookie': login.cookie
    }

files = {
    'data_mode':(None,""),
    'name': (None,"hotnewfeeds"),
    'num':"30",
}

params = {
        'userid': "0",
        'time': login.time,
        'rand': login.rand,
        'platform': login.platform,
        'version': login.version,
        'guid': guidFeed,
    }
feedRes = login.sendReq("https://live.huajiao.com/feed/getHotNewFeeds", "get", headers=headers, params=params, files=files)
#print(feedRes)

wantFeed = feedRes.get("data").get("feeds")[1]
print(wantFeed)

relateId = wantFeed.get("feed").get("relateid")
favorite = wantFeed.get("feed").get("favorited")
#print(relateId, favorite)

