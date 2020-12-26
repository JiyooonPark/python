# basics
a = [1,2,3]
print(a)
a1 = [1,2,3,[1,2,3]]
print(a1)
a2 = [1,2,'hello','hi']
print(a2)
    #empty list
a3 = list()
print(a3)

#indexing and slicing
    #statrs from 0
b = [1,3,5,67,8,[4,3,2,3,2]]
b1 = b[3]+b[4]
print(b1)
    #double indexing (can do tri-indexing)
b2 = b[-1][-2]
print(b2)

#list add, repeat
c = [1,2,3,4]
c1 = [4,5,6,7]
    #add
print(c+c1)
    #repeat
print(c*3)
    #length
print(len(c))
    #cannot add int + str
# print(c[1]+'hi')
print(str(c[1])+'hi')

#list modification, remove
    #edit : perminant modification
d = [1,2,3,4,5,6,7]
print(d)
d[2]=100
print(d)
    #del object
del d[4]
print(d)
del d[2:]
print(d)

#functions related to lists
e = [1,2,3,4]
    #append one element to list
e.append(100)
print(e)
        #can append lists to lists
e.append([222,22,2])
print(e)
    #sort
e[-1].sort()
print(e)
    #reverse
e[-1].reverse()
print(e)
    #index
        #if not in list returns error
e1 = e.index(2)
print(e1)
    #insert in position
e.insert(-1,100)
print(e)
    #remove by value
e.remove(2)
print(e)
    #pop
print(e.pop())
    #count values
print(e.count(0))
    #extend(list)
e.extend([2,2,2,1,1,1,1,1])
print(e)