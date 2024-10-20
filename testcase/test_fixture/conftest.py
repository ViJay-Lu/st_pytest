import pytest

@pytest.fixture(scope="function")
def my_fixture_1():
    print("enter my_fixture_1 function\n")
    #yield :后置
    yield
    print("exit my_fixture_1 function\n")