#basics
a = (2,3,4)
print(a)
    #need a comma when it only has one element
a1 = (1,)
print(a1)

#handling tuples
    #no del
    #no edits
    #indexing
b=a[1]
print(b)
b1 = a[:2]
print(b1)
    #adding
b2 = (9,8,7)
print(a+b2)
    #repeat
print(a*2)
    #length
print(len(a))