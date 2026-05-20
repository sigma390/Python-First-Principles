

#functions accept args
#functions are Objects means we can return a function

#normal function
def func():
    print("We are inside a function")

func()


#function inside a function and calls  , also Optional params
def sum (x , y , z , q = None):
    s = x + y
    def multi(s , z):
        return s*z;
    return multi(s,z)



#function can return multiple values
def tup(x , y):
    return x*y, x+y , x**y


r1,r2,r3 = tup(2,6)



#cool thing

def f1(x):
    def f2():
        print(x)
    return f2

f1(907798989789686)() # () ()<=== means a call


print(tup(2,6))
print(sum(2,3, 9))
print(r1,r2,r3)





