#where the variables are saved
a = [12,3,4,5,1,11]
    #id is the address the computer uses to store the data
print(id(a))
    #shares addresses if =
b = a
print(id(b))
    #copy list without sharing
        #using [:]
b1 = a[:]
print(id(b1))
        #using copy
from copy import copy
b2 = copy(a)
print(id(b2))

#many ways to make variables
c1, c2 = (2,1)
print(c1, c2)
[c3, c4] = [3,4]
print(c3, c4)

c5 = c6 = 100
    #swap
c2 , c5 = c5, c2
