import pytest

if __name__ == '__main__':
    #主函数模式
    pytest.main(['-vs','E:\workspace\py\st_pytest\\testcase','--reruns=2'
                    ,'--html=report.html','-n=3','--maxfail=2','-k=get'])