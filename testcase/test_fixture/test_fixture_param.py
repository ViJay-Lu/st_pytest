import pytest
"""
scop:表示作用域
params:参数化
autouse:是否自动执行
ids:当使用params参数化时，给每一个变量设置一个变量名、意义不大
name:表示被@pytest@fixture标记的方法取别名


值得注意的是：
1，这里的参数request是固定写法
2，要取params中的值时，如果：return request.param，则取不到值
   需要将返回的内容写在yield后。这不会影响前后置
def my_fixture(request):
    print("\nthis is first")
    yield request.param
    print("\nthis is last")
"""
#@pytest.fixture(scope="function",params=['jack','yoyo','vijay']
                #,autouse=False,ids=['jk','yy','vj'],name='aaa')
"""
#原本的练习代码挪到conftest.py中
@pytest.fixture(scope="fuction",autouse=True)
def my_fixture(request):
    print("\nthis is first")
    yield 
    print("\nthis is last")
"""


#def test_vijay_func(my_fixture):
#用了别名参数name之后，原来的名称就用不了了。会直接报错 fixture 'my_fixture' not found
def test_vijay_func(my_fixture):
    print("this is vijay func " + "," + str(my_fixture))

def test_yoyo_func():
    print("this is yoyo func")

def test_lilian_func():
    print("this is lilian func")