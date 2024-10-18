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

scop:表示作用域
params:参数化
autouse:是否自动执行
ids:当使用params参数化时，给每一个变量设置一个变量名、意义不大
name:表示被@pytest@fixture标记的方法取别名
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
#
#遇到的坑：当在窗口直接点击图标运行时，打印数据混乱，enter前置出现在了最后面
#换成命令行方式运行则正常
#
@pytest.fixture(scope="function")
def my_fixture():
    print("enter my_fixture function\n")
    #yield :后置
    yield
    print("exit my_fixture function\n")

def test_equal(my_fixture):
    a = 2
    b = 2
    print('enter test_equal function\n')
    assert a == b

def test_req_get(my_fixture):
    params = {
        "shouji": "15823642154",
        "appkey": "54dsfsa5g456"
    }
    rsp = requests.get("http://sellshop.5istudy.online/sell/shouji/query", params=params)
    #rsp_json = rsp.json()
    # assert rsp_json['msg'] == "ok"
    print('enter test_req_get function\n')
    assert rsp.status_code == 200
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


class TestFixture:
    def test_func(self):
        a = 2
        b = 2
        assert a == b
