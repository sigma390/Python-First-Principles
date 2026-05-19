

#range function
# range(start, stop , step)




for i in range (10):
    print(i);


print("\n")



for i in range(1,9,2):
    print(i)

print("\n")

for i in range(-10, 0, 1):
    print(i)

#Looping through the list

x = [1,2,3,4,5]

print("\nPrinting the list : \n")
for i in x :
    print(i)

#keep in touch with the index
print("\nHaving the Track of index : \n")
for i in range(len(x)):
    print(x[i])

#enumerate
print("\nThis is way of enumerate : \n")
for i, element in enumerate(x):
    print(i, element)