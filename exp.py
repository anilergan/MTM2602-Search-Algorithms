
"""
root = (0,0)
child1 = [(0,1), (0,2), (1,0)]

child11 = [(1,1), (0,3)]
child12 = [(0,4), (1,2), (2,2)]
child13 = [(2,0)]

child211 = [(1,3)]
child212 = [(1,3), (0,5)]
child121 = [(1,4)]
child122 = [(2,3)]
child123 = [(3,2)]
child231 = [(2,1), (3,0)]

# First Depth
path = [root]
parent = path[0]
path.pop(0)

for c in child1:
    new_path = (parent, c)
    path.append(new_path)

print(path) # GOOD

print('-'*40)

# Second Depth
parent = list(path[0])
path.pop(0)

for c in child11:
    parent.append(c)
    new_path = tuple(parent)
    path.append(new_path)

print(path)
print('-'*40)
for p in path:
    print(p[-1])

print('-'*40)
target = (1,1)
for index, p in enumerate(path):
    if p[-1] == target: print(index)

"""

from numpy import array as arr

test1 = 0.1799047
test2 = 0.30217052
test3 = 0.17437959
test4 = 0.24337745
test5 = 0.28180456

ortalama = (test1 + test2 + test3 + test4 + test5) / 5


print(round(ortalama, 5))












