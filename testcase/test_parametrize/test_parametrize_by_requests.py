import os
import sys

import pytest
import requests

pythonpath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, pythonpath)

from read_config_file.read_data import read_data

@pytest.mark.parametrize("shouji,appkey",read_data("mobile_params"))
def test_req_get(shouji,appkey):
    params = {
        "shouji": shouji,
        "appkey": appkey
    }
    rsp = requests.get("http://sellshop.5istudy.online/sell/shouji/query", params=params)
    # rsp_json = rsp.json()
    # assert rsp_json['msg'] == "ok"
    if appkey == "adgadfgdghf3":
        assert rsp.status_code == 200
        assert rsp.json()["msg"] == "ok"
        assert rsp.json()["result"]["shouji"] == "13425657884"
        assert rsp.json()["result"]["company"] == "中国移动"
    elif appkey == "564564gdsgff":
        assert rsp.status_code == 200
        assert rsp.json()["msg"] == "ok"
        assert rsp.json()["result"]["shouji"] == "15896587456"
        assert rsp.json()["result"]["company"] == "中国移动"