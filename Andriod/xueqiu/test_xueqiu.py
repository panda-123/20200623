#coding=UTF-8
#作者:herui
#时间:2020/5/23 20:12
#功能:

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import unittest

class test_XueQiu(unittest.TestCase):

    def setUp(self):
        print("setup")
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "MIMax"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["grant"] = True


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(8)

    def test_search_stock(self):
        self.driver.find_element_by_id("tv_agree").click()
        self.driver.find_element_by_id("home_search").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id("search_input_text").send_keys("JD")
        self.driver.find_element_by_xpath("//*[@text='京东']").click()
        self.driver.find_element_by_id("add_attention").click()


