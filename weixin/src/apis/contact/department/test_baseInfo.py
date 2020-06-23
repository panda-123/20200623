#ecoding=utf-8
# author:herui
# time:2019
import requests
def test_get_access_token():
    url = r'https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
    my_para={
        'corpid':'ww9db5398ae0670287',
        'corpsecret':'NMbkH4d-2zyASPvzCiUBx99fOGIF2tAXo8-r4IM1WaY'
    }
    res = requests.get(url,params=my_para,verify=False)
    accessTokenId = res.json()
    print(accessTokenId)
    return accessTokenId['access_token']
def test_get_mediaId():
    access_token = test_get_access_token()
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+access_token
    # file =
    msg = {
        "touser": "UserID1|UserID2|UserID3",
        "toparty": "PartyID1|PartyID2",
        "totag": "TagID1 | TagID2",
        "msgtype": "image",
        "agentid": 1,
        "image": {
            "media_id": "MEDIA_ID"
   },
   "safe":0
}