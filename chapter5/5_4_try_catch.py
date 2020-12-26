#basic
try:
    print(4/0)
except:
    print("No can do")

#1
try:
    print(4/0)
except ZeroDivisionError as e:
    print(e)


#sevral errors
    #1
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

    #2
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

#raise error
class Bird:
    def fly(self):
        raise NotImplementedError #raise error if not overridden

#make error class
class MyError(Exception):
    # exception e
    def __str__(self):
        return "허용되지 않는 별명입니다."
    pass
if True:
    raise MyError
else:
    pass
