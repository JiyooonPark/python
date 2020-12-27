money = True
if money:
    print("I have money")
else:
    print("I don't have money")

money = 2000
if money <=1000:
    print("cannot buy anything")
elif money <=2000:
    print("can buy one drink")
else:
    print("you are rich")

# and or not
card = True
if money >= 2000 and card:
    print("okee")
else:
    print("nope")

# lists and in
l = [1,2,3,4,5]
if 1 in l:
    print("one")
else:
    print("no")

#strings, tuples also

if 'j' in 'jiyoon':
    print("jiyooooon")
else:
    print("oo")

#pass
if True:
    pass
else:
    print("No")
