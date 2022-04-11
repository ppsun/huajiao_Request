import login
import get_relateId
import getUserFeed


f3 = open('/user_file.txt')
userId = f3.readline()
#print(userId)


class Feed(object):

    def __init__(self, feedId, isFav):
        self.feedId = feedId
        self.isFav = isFav

    def changeFavorite(self):

        if userId != "" and userId != None:
            #点赞guid
            guidFav = login.getGuid(login.userid)

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

            params = {
                'userid': login.userid,
                'time': login.time,
                'rand': login.rand,
                'platform': login.platform,
                'version': login.version,
                'guid': guidFav,
                'relateid': self.feedId
            }

            if self.isFav == False:
                add = login.sendReq("https://live.huajiao.com/favorite/add", "get", headers=headers, params=params)
                return add
            elif self.isFav == True:
                delet = login.sendReq("https://live.huajiao.com/favorite/delete", "get", headers=headers, params=params)
                return delet
            else:
                print("favorite不能为空")
        else:
            print("请先登录")


#feed1 = Feed(get_relateId.relateId, get_relateId.favorite)
#res = feed1.changeFavorite()
#print(res)

feed2 = Feed(getUserFeed.userFeedId, getUserFeed.userFeedFav)
userRes = feed2.changeFavorite()
print(userRes)



