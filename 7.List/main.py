


#lists

#lists are Mutable means x[0] = "8" that changes its memory location not copy
x = [1, "Hellow" , 7.8];
y = [9,10]


#list methods

x.append("New element")
x.remove(1);
x.extend(y)

for i in x:
    print(i , end = ",")

print("\n")
print(x[2])



#Tupel are Immutable cant append , change , delete , reassign and all

a  = (1,2,5)
for i in a:
    print(i**2)