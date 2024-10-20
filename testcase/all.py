import os
import pytest
import platform
from get_platform.get_platform import get_platform

if __name__ == '__main__':
    #主函数模式
    if get_platform() == "windows":
        #pytest.main(['-vs','E:\workspace\py\st_pytest\\testcase','--reruns=2'
                    #,'--html=report.html','-n=2','--maxfail=2','-k=get'])
        pytest.main()
    elif get_platform() == "macos":
        #pytest.main(['-vs','/Users/lucas/python/st_pytest/testcase'
                    #,'--reruns=2','--html=report.html','-n=2','--maxfail=2','-k=get'])
        pytest.main()
    #allure generate 固定命令
    # ./json_temp 临时json格式报告路径
    # -o    输出：output
    # ./report  生成allure报告的路径
    # --clean   清空原来的报告
    os.system('allure generate ./json_temp -o ./report --clean')