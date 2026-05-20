

x = [i for i  in range(7)]
y = [i*3 for i  in range(7)]

z = [ i for i in range(200) if i%5==0 ]

#for dict also this works

a = { j : 2 for j in range(30) if j%2==1} #{element : initialiser for element if condtion }

b = {k for k in range(10)}
print(x)
print(y)
print(z)
print(a)
print(b)