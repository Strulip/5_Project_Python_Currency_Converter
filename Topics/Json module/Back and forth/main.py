#  You can experiment here, it won’t be checked
import json

a = {42: "Life, the Universe, and Everything"}
b = [{"race": "elf", "class": "bard"}, {"race": "dwarf", "class": "monk"}]
c = {"decimal": 10, "binary": 1010, "hexadecimal": "A"}
d = {True: ["Water is wet", "Earth revolves around the Sun"], False: ["We live on Jupiter", "x is not equal to x"]}

a_json_str = json.dumps(a)
b_json_str = json.dumps(b)
c_json_str = json.dumps(c)
d_json_str = json.dumps(d)

a_back = json.loads(a_json_str)
b_back = json.loads(b_json_str)
c_back = json.loads(c_json_str)
d_back = json.loads(d_json_str)

print(a == a_back)
print(b == b_back)
print(c == c_back)
print(d == d_back)