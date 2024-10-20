import pytest
#和@pytest.fixtrue结合使用，用于全局范围。不需要任何import导入操作
#可以在不同文件使用同一个fixtrue函数
#原则是conftest.py要和测试用例放在同一层目录
@pytest.fixture(scope="function")
def my_fixture():
    print("\nenter my_fixture function")
    yield
    print("\nexit my_fixture function")