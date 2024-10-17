def test_one():
    expect = 1
    actual = 2
    assert expect == actual


def test_two():
    expect = 1
    actual = 1
    assert expect == actual

#只识别test开头的方法
def three():
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