# if something is there or not
#best for Lookups
#constant time lookups

x = set()

s1 = {4,32,4,4,4,1}
s2 = {9,10,1}
print(s1)

s1.add(5)
s1.remove(4)

print(s1)
print(4 in s1)
print(1 in s1)
print(s1.union(s2))
print(s1.difference(s2))
print(s1.intersection(s2))