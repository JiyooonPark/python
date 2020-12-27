a = "Hello World"
b = 'Hello World'
c = '''Hello 
World
'''
d = """Hello
World
"""
e = 'Hello \'World'
# print(a,b,c,d,e)

#string concatenation
f = a +" "+ b
# print(f)

#String repeat
g = "a"*10
# print(g)

#String len
# print(len(g))

#String slicing
h = a[4:9]
    #[start:end+1]
    #[-1] from the back
h1 = a[-5:-1]
# print(h)
# print(h1)

#String replacement
i = a[:6]+"Me"
# print(i)

#String formatting
j = "2 + 2 = %d" % 4
j1 = "Hello I am %s" % "jiyoon"
    # %% is % itself
j2 = "%d%%" % 100
# print(j)
# print(j1)
# print(j2)

#String formatting - length
    #+ aligns to right - aligns to left
k = ".%30s." % "HelloIamMeMeMeMeMeMeMeMe"
k1 = ".%-30s." % "HelloIamMeMeMeMeMeMeMeMe"
# print(k)
# print(k1)

#String formatting - using functions
    #by index
l = "I ate {0} apples".format("ten")
l1 = "I ate {0} apples and {1} lemon".format("ten","one")
    #by name
l2 = "I ate {a} apples and {b} lemon".format(a="ten",b="one")
    #by both
l3 = "I ate {0} apples and {b} lemon".format("ten",b="one")
    #align
        #left
l4 = "{0:<10}".format("hi")
        #right
l5 = "{0:>10}".format("hi")
        #center
l6 = "{0:^10}".format("hi")
# print(l)
# print(l1)
# print(l2)
# print(a) # the var in .format() dows not change the global var
# print(l3)
# print(l4)
# print(l5)
# print(l6)
    #align and fill with =
l7 = "{0:=^10}".format("hey")
print(l7)
    #align and fill with a
l8 = "{0:a^10}".format("hey")
print(l8)

#floating points formatting
m100 = 3.14159232132132
m = ".{0:0.4f}.".format(m100)
m1 = ".{0:^10.4f}.".format(m100)
# print(m)
# print(m1)

#String f formatting
name = "JyPark"
age = 21
n = f"{name:=^10} is {age} years old"
print(n)

#Functionsrelated to strings
    #count() :
o = a.count('e')
print(o)
    #find
        #if not found returns -1
o1 = a.find('l')
print(o1)
    #index : similar to find but
        #if not found returns error
o2 = a.index('e')
    #join
o3 = "/".join('abcde')
o4 = "/".join(['a','b','c','d'])
print(o3)
print(o4)
    #toUpperCase (in java)
o5 = a.upper()
print(o5)

    #toLowerCase (in java)
o6 = a.lower()
print(o6)
    #strip : erase spaces
o7 = a.strip()
        #left only
o8 = a.lstrip()
        #right only
o9 = a.rstrip()
    #replace string/word
o10 = a.replace("Hello", "hehe")
print(o10)

#Split
p = "Eh is a Canadian word-ish"
p1 = p.split(" ")
print(p1)