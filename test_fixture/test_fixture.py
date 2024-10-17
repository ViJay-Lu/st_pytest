"""
fixture是pytest用于将测试前后进行预备、清理工作的代码机制处理。
相对于setup和teardown：
    fixture命名更加灵活、局限性较小
    conftest.py配置里面可以实现数据共享，不需要import就能自动找到一些配置

@pytest.fixture
(scop="function") 每一个函数或方法都会调用
(scop="class") 每一个类调用一次
(scop="module") 每个py文件调用一次
(scop="session") 多个文件调用一次

作用范围：session > module > class > function
"""

import requests
import pytest
"""
eg1:
#scope参数默认是function,可省略参数
@pytest.fixture()
    def func():
    print("this is func")

#使用时，需将func传入要测试函数的参数列表中
def test_equal(func):
    a = 2
    b = 2
    assert a == b
    
#参数autoouse=True、代表文件中所有测试函数都使用func
@pytest.fixture(scope="function", autouse=True)

#只在类中调用
@pytest.fixture(scope="class")
"""

#在整个py文件中调用一次
@pytest.fixture(scope="module",autouse=True)
def func():
    print("this is fixture func")

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
    a = 2
    b = 2
    assert a == b

class TestFixture:
    def test_func(self):
        a = 2
        b = 2
        assert a == b
