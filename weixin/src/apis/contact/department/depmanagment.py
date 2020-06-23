#ecoding=utf-8
# author:herui
# time:2019

import logging
from apis.baseapi import BaseAPI
from initialization.sysconfig import sys_config

class DepManagment(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("init department managment API")
        self.create_dept_url = sys_config.get('contact_para', 'create_dep_url')
        self.dep_secret = sys_config.get('contact_para', 'secret')
        self.update_dept_url = sys_config.get('contact_para', 'update_dep_url')

    def create_dept(self):
        new_part = {
            "name": "tester",
            "parentid": 1,
            "order": 1,
            "id": 6
        }

        param = {"access_token":self.get_token(self.dep_secret)}
        logging.debug("url:"+str(self.create_dept_url))
        logging.debug("para:" + str(param))
        self.post_json(self.create_dept_url,new_part,params=param)

    def get_create_dept_res(self):
        return self.get_response()

    def update_dept(self):
        update_info = {
            "id": 5,
            "name": "和瑞20191108",
            "parentid": 1,
            "order": 1
        }
        param = {"access_token": self.get_token(self.dep_secret)}
        self.post_json(self.update_dept_url, update_info, params=param)

    def get_update_dept_res(self):
        return self.get_response()

