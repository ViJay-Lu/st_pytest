import pytest
import platform
from get_platform.get_platform import get_platform

if __name__ == '__main__':
    #主函数模式
    if get_platform() == "windows":
        pytest.main(['-vs','E:\workspace\py\st_pytest\\testcase','--reruns=2'
                    ,'--html=report.html','-n=3','--maxfail=2','-k=get'])
    elif get_platform() == "macos":
        pytest.main(['-vs','/Users/lucas/python/st_pytest/testcase'
                    ,'--reruns=2','--html=report.html','-n=3'
                    ,'--maxfail=2','-k=get'])