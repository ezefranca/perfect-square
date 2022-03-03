import math 

perfect = []
for i in range(0,100001):
    root = math.sqrt(i)
    if int(root + 0.5) ** 2 == i:
        print(i, "is a perfect square")
        perfect.append(i)
    else:
        print(i, "is not a perfect square")

print(len(perfect))

# 100 - 11
# 1000 - 32
# 10000 - 101
# 100000 - 
