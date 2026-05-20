#Key value Pairs



x = {"a":10}
x[1] = ["this", "is","dict"]

print('a' in x)
print(x["a"])
print(x)
print(list(x.values()))
print(list(x.keys()))

for key, value in x.items():
    print(key, value)

for key in x :
    print(key)