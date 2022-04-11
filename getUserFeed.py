
import login

userFeedGuid = login.getGuid(login.userid)

headers = {
    "Host": "live.huajiao.com",
    "Cookie": login.cookie,
    "User-Aent": "living/8.2.3 (iPhone; iOS 15.3.1; Scale/3.00)",
    "Accept": "*/*",
    "Accept-Language": "zh-Hans-CN;q=1",
    "Accept-Encoding": "gzip",
    "Connection": "keep-alive"
    }
params = {
    "userid": login.userid,
    "time": login.time,
    "rand": login.rand,
    "platform": login.platform,
    "version": login.version,
    "guid": userFeedGuid,
    "uid": "243059863"
    }

userFeed = login.sendReq("https://live.huajiao.com/feed/getUserFeeds", "get", headers=headers, params=params)
wantUserFeed = userFeed.get("data").get("feeds")[0]
print(wantUserFeed)

userFeedId = wantUserFeed.get("feed").get("relateid")
userFeedFav = wantUserFeed.get("feed").get("favorited")
print(userFeedId, userFeedFav)