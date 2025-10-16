'''
book:資訊社會必修的12堂python通識課
date:114/10/16
'''

# 1. 9*9乘法表 ex1
# format format：字串格式化、f-string
for i in range(1, 10):
    for j in range(1, 10):
        print("{}x{} = {}".format(i,j,i*j))
    print()

print()

# 9*9乘法表 ex2
# use f-string
for j in range(1, 10):
    for i in range(1, 6):
        print(f"{i}x{j} = {i*j:<2}", end="\t") #結果寬度固定（<2 左對齊，保持整齊）。
    print("\t", end="") #中間空一格
    for i in range(6,10):
        print(f"{i}x{j}={i*j:<2}", end="\t")
    print()

print()

# 9*9乘法表 ex3 分兩邊
# []是list，僅有2,6值
for i in [2,6]:
    for j in range(1,10):
        print("{}x{} = {:2d}".format(i,j,i*j), end="")

# python dict
dict1 = {"apple": 1, "banana": 2, "cherry": 3}
dict2 = dict(cherry=1, banana=2, apple=3)
dict3 = dict([("apple", 1), ("banana", 2), ("cherry", 3)])

print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)

