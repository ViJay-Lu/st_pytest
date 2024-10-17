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
fd = open(".\\data.yaml",encoding="utf-8")
data = yaml.safe_load(fd)
print(data)