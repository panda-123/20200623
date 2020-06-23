#ecoding=utf-8
# author:herui
# time:2019

from apis.contact.department.depmanagment import DepManagment

class TestCreateDep:

    def test_create_new_dep(self):
        dept_managment = DepManagment()
        dept_managment.create_dept()
        create_res = dept_managment.get_response()
        assert create_res.get("errmsg") =="created"
