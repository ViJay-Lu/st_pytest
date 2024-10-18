import pytest
import requests

#测试类不能有init方法
class TestSetupClass:
    # 在类中前后执行一次
    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def test_req_get(self):
        params = {
            "shouji": "15823642154",
            "appkey": "54dsfsa5g456"
        }
        rsp = requests.get("http://sellshop.5istudy.online/sell/shouji/query", params=params)
        #rsp_json = rsp.json()
        assert rsp.status_code == 200
        #assert rsp_json['msg'] == "ok"
        assert rsp.json()["msg"] == "ok"
        assert rsp.json()["result"]["shouji"] == "15823642154"


    def test_req_post(self):
        param = {
            "shouji": "13963241566",
            "appkey": "0c818521d38759el"
        }
        rsp_param = requests.post("http://sellshop.5istudy.online/sell/shouji/query",
                                  params=param)

        assert rsp_param.status_code == 200
        assert rsp_param.json()["msg"] == "ok"

    def test_equal(self):
        a = 1
        b = 1
        assert a == b

"""
============================= test session starts =============================
collecting ... collected 3 items

test_setup_class.py::TestSetupClass::test_req_get 
test_setup_class.py::TestSetupClass::test_req_post 
test_setup_class.py::TestSetupClass::test_equal 

============================== 3 passed in 0.72s ==============================
setup_class
PASSED                 [ 33%]PASSED                [ 66%]PASSED                   [100%]teardown_class
"""