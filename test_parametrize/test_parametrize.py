"""
单词循环
@pytest.mark.parametrize("a",["b"])
def test_parametrize(a):
    print(a)
"""
import pytest

#单参数、单词循环
@pytest.mark.parametrize("name",["vijay"])
def test_parametrize_01(name):
    assert name == "vijay"

#多参数、多次循环
@pytest.mark.parametrize("name,age",[["vijay",32],["yoyo",2],["lilian",30]])
#@pytest.mark.parametrize("name,age",[("vijay",32),("yoyo",2),("lilian",30)])
def test_parametrize_02(name,age):
    print(f"{name} {age} years old")
    if name=="vijay":
        assert age == 32
    elif name=="yoyo":
        assert age == 2
    elif name=="lilian":
        assert age == 30