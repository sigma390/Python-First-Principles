

a = 5 #integer
b = 3.4 #float
c  = "Hello World" #string
c = a + b 



#string concatenation
a = "hello" "world"
d = "hello" * 5


d = a # reassigning the value of a to d
print(c)
print(a)
print(d,end='\n')


expense_request = "this is expense request for 100 dollars" #always use a snake_case


#scope of a variable

# use word global to make vqariable global 

#ex local scope but then we made it global inside a function

x = "global"

def func():
    global x  
    x = "we made this global"
func()

print(x)