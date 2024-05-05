
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

w = arr([[1,2,3], [4,5,6], [7,8,9]])

u = [1,2,3]
i = 10

listem = []

listem.append((tuple(u), i))



print(listem)

# print(u)












