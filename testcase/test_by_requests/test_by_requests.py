import pytest
import requests

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

test_by_requests.py::test_req_get <- test_by_qequests\test_by_requests.py 
test_by_requests.py::test_req_post <- test_by_qequests\test_by_requests.py 

============================== 2 passed in 0.76s ==============================
PASSED [ 50%]PASSED [100%]
"""