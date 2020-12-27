# basic for loop
a = [1,2,3,4,5]
for i in a:
    print(i)

b = [(1,'one'),(2,'two'),(3,'three')]
for (i,j) in b:
    print(j)

c = [90,100,98,85,80]

for i in c:
    if i>=95:
        print("A+")
    elif i>=90:
        print("A")
    elif i>=80:
        print("B+")
    else :
        print("Pass")

for i in range(0,10):
    print(i)

d = [1,2,3,4,5]
d1 = [i**2 for i in d if i%2 == 0]
print(d1)

e = [x*y for x in d for y in d]
print(e)