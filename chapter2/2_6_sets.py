#basics
a = set([1,2,3])
print(a)
a1 = set("hehehehehe")
print(a1)
    #no repeats
    #need to cast it to list or tuple to use

#union, sum, ...
    #intersection
b = set("abskfjfdksla")
b1 = set("dfdsajasks")
print(b&b1)
print(b.intersection(b1))
    #union
b2 = b | b1
b3 = b.union(b1)
print(b2)
print(b3)
    #difference
b4 = b - b1
b5 = b.difference(b1)
print(b4)
print(b5)

#add, remove
    #add
b.add(100)
print(b)
    #add multiple
b.update([2,1,1,1,2,3,32,1,2])
print(b)
    #remove
b.remove(2)
print(b)