import pytest
import requests

#开始于模块始末，生效一次
def setup_module(module):
    print("setup_module")

def teardown_module(module):
    print("teardown_module")

def test_req_get():
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


def test_req_post():
    param = {
        "shouji": "13963241566",
        "appkey": "0c818521d38759el"
    }
    rsp_param = requests.post("http://sellshop.5istudy.online/sell/shouji/query",
                              params=param)

    assert rsp_param.status_code == 200
    assert rsp_param.json()["msg"] == "ok"

"""
============================= test session starts =============================
collecting ... collected 2 items

test_setup_module.py::test_req_get 
test_setup_module.py::test_req_post 

============================== 2 passed in 0.71s ==============================
setup_module
PASSED                                [ 50%]PASSED                               [100%]teardown_module

"""