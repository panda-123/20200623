#ecoding=utf-8
# author:herui
# time:2019

#ecoding=utf-8
# author:herui
# time:2019

from apis.contact.department.depmanagment import DepManagment

class TestCreateDep:

    def test_update_depinfo(self):
        up_dept_managment = DepManagment()
        up_dept_managment.update_dept()
        update_res = up_dept_managment.get_response()
        assert update_res.get("errmsg") == "updated"