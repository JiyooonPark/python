#dictionary aka hash, associative array
    #cannot use list as key
a = {'a':'A', 'b':'B','c':'C'}
print(a)
    #can put diverse elements in dic
a1 = {1:[1,2,3], 2:'hello', 3:(9,1,2)}
print(a1)

#add, del
    #add
a[2]=44
print(a)
    #del
del a['a']
print(a)

#how to use dic
print(a['b'])

#functions related to dic
print(a.keys())
    #to use it, throw it into a list
b = list(a.keys())
print(b)
b1 = list(a.values())
print(b1)
b2 = list(a.items())
print(b2)
    #get is similar to [] but does not return an error
print(a.get(100))
    #get set default value
print(a.get(100,200))
    #search if key in list
print(3 in a)