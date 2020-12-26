# basic functions
def add(x,y):
    print("%d + %d = %d" % (x,y,x+y))
    return x+y

add(y = 10,x = 20)
add(10,20)

# function with many arguments
def add_many(*args):
    result = 0
    for i in args:
        # print(i)
        result += i
    print(result)
    return result

add_many(3,2,1,5,1,5,3,3333,333,4,32,4,24,2)

#function with many params -> dictionary
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 19, b = 100)

#return
def r1():
    return 1, 2 #returns a tuple
r1a = r1()
print(r1a)
    #if you want to return 2 vars, assign two return values
r11, r12 = r1()
print(r11, r12)

#default value
def r2(a=True):
    print(a)
r2(False)

#lambda
hello = lambda a, b : a+b
print(hello(1,22))