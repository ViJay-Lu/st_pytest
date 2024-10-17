import pytest
import requests

#对不在类中的测试函数生效
def setup_function():
    print("setup_function")

def teardown_function(module):
    print("teardown_function")

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

def test_equal():
    a = 1
    b = 2
    assert a == b

"""
============================= test session starts =============================
collecting ... collected 3 items

test_setup_function.py::test_req_get 
test_setup_function.py::test_req_post 
test_setup_function.py::test_equal 

========================= 1 failed, 2 passed in 0.88s =========================
setup_function
PASSED                              [ 33%]teardown_function
setup_function
PASSED                             [ 66%]teardown_function
setup_function
FAILED                                [100%]
test_setup_function\test_setup_function.py:34 (test_equal)
1 != 2

预期:2
实际:1
<点击以查看差异>

def test_equal():
        a = 1
        b = 2
>       assert a == b
E       assert 1 == 2

test_setup_function.py:38: AssertionError
teardown_function
"""