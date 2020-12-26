# write function
    #basic
f = open('hellow.txt','w')
for i in range(0,5):
    data = "%d th row\n" % i
    f.write(data)
f.close()

    #append
f = open('hellow.txt','a')
for i in range(5,10):
    data = "%d th row\n" % i
    f.write(data)
f.close()

#read functions
f=open('hello.txt','r')
while True:
    line = f.readline();
    if not line: break
    # print(line)
f.close()

    #read lines functions
f=open('hello.txt','r')
lines = f.readlines();
for line in lines:
    print(line)
f.close()

    #read function
f=open('hello.txt','r')
print(f.read())
f.close()

#using with functions to automize file input, output
with open("hello.txt",'r') as f:
    f.read()

