import pytest

#pytest默认是顺序执行的，要想改变测试顺序则要使用@pytest.mark.run(order=1)(mark标记方法)
"""
collecting ... collected 3 items

test_one.py::test_three 
test_one.py::test_one 
test_one.py::test_two 
"""
@pytest.mark.run(order=2)
@pytest.mark.smoke
def test_one():
    expect = 1
    actual = 2
    assert expect == actual


@pytest.mark.run(order=3)
@pytest.mark.order
def test_two():
    expect = 1
    actual = 1
    assert expect == actual

#只识别test开头的方法,所以这个函数不会被执行
def three():
    expect = 1
    actual = 1
    assert expect == actual

@pytest.mark.run(order=1)
def test_three():
    expect = 1
    actual = 1
    assert expect == actual


@pytest.mark.skip(reason="无条件跳过test_four")
def test_four():
    expect = 1
    actual = 1
    assert expect == actual

age = 32
name = 'vijay'
@pytest.mark.skipif(age>=18 and name == 'vijay',reason="条件忽略test_five")
#@pytest.mark.skipif(name != 'vijay',reason="条件忽略test_five") #也可以多条件使用,and、or 都可
def test_five():
    expect = 1
    actual = 1
    assert expect == actual

"""
============================= test session starts =============================
collecting ... collected 2 items

test_one.py::test_one 
test_one.py::test_two 

========================= 1 failed, 1 passed in 0.34s =========================
FAILED                                             [ 50%]
test_one\test_one.py:0 (test_one)
1 != 2

预期:2
实际:1
<点击以查看差异>

def test_one():
        expect = 1
        actual = 2
>       assert expect == actual
E       assert 1 == 2

test_one.py:4: AssertionError
PASSED                                             [100%]
"""