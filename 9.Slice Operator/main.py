

# [start:stop:step] // Stop is not inclusive , start is inclusive

x  = [0,1,8,3,4,5,6,7,8,9]

sl_1 = x[:5]; #default step is 1
sl_2 = x[1:7:2] #stepping forwards
sl_3 = x[7:0:-1] #stepping backwards

#simplest method to reverse a list or a string

y = x[::-1];



for x in sl_1:
    print(x)

print("This is slice with the step : \n")
for x in sl_2:
    print(x)

print("This is slice with the -ve step : \n")
for x in sl_3:
    print(x)