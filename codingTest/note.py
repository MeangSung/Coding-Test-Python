d = [1,3,6,7]
c = [1,3,6,7,5]

tree = []
tree.append(d)
tree.append(c)
tree.sort()
d.pop()
print(d)
print(tree)