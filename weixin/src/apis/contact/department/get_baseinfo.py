#ecoding=utf-8
# author:herui
# time:2019
import requests
def get_access_token():
    url = r'https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
    my_para={
        'corpid':'ww9db5398ae0670287',
        'corpsecret':'NMbkH4d-2zyASPvzCiUBx99fOGIF2tAXo8-r4IM1WaY'
    }
    res = requests.get(url,params=my_para,verify=False)
    accessTokenId=res.json()
    print(accessTokenId)