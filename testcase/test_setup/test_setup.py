import pytest
#我的pytest版本为： 8.3.3，查看方式：pytest --version
#看视频博主调用的是setup和teardown,整个版本不生效，应该已经弃用了。再没有研究。还是用之前的setup_method

class TestSetup:
    def setup_method(self):
        print('\n enter function setup,每个用例之前的初始化工作')

    def test_01(self):
        print('\n enter function test_01')

    def test_02(self):
        print('\n enter function test_02')

    def test_03(self):
        print('\n enter function test_03')

    def teardown_method(self):
        print('\n enter function teardown，每个用例之后的收尾工作')

