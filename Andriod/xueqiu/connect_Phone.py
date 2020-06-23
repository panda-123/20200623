#coding=UTF-8
#作者:herui
#时间:2020/5/29 22:34
#功能:通过WIFI连接手机，进行元素定位

import uiautomator2 as u2

# 使用命令
# python -m weditor
d = u2.connect('192.168.31.137')
print(d.info)
