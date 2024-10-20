"""
对象：
key:
  child-key:value
  child_key1:value1
  == {'key':{'child':'value','child_key1':'value1'}}

数组：
key:
  - A
  - B
  - C
=={'KEY':[A,B,C]}

组合：
key:
  -child-key:value
   child-key1:value1
=={'key':[{'child-key':'value','child-key1':'value1'}]}

嵌套：
key:
  -
    -A
    -B
    -C
=={'key':[[A,B,C]]}
"""
import yaml
from get_platform.get_platform import get_platform

"""
{'person': {'name': '张三', 'age': 10}, 'persons': ['张三', '李四', '王麻子'],
 'person_info': [{'name': '王五', 'age': 19}], 'vec': [['语文', '数学', '英语']]}
"""
def read_data(args):
    if get_platform() == "windows":
        fd = open("E:\workspace\py\st_pytest\config\data.yaml", encoding="utf-8")
    elif get_platform() == "macos":
        fd = open("/Users/lucas/python/st_pytest/config/data.yaml",encoding="utf-8")
    data = yaml.safe_load(fd)
    return data[args]
