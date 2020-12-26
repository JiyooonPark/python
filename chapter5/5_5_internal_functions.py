#abs
print(abs(-102))

#all
    #returns True iff all elements are True
    #returns True if empty
print(all([1,2,2,3,31,0]))

#any
    #returns True if any element is True
print(any([1,0]))

#chr
    #takes ascii code and returns the char
print(chr(98))

#dir
    #dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다
print(dir([1,23,1]))

#divmod
print(divmod(10,3))

#eumerate
    #returns index and value
for (i, val) in enumerate([1,2,3,4,5,6]):
    print(i,':', val)

#eval
    #returns executed version
print(eval("2+1"))

#filter
    #(function, param) returns onlt values that are true in param according to function
def positive(l):
    return l>0
print(list(filter(positive, [-1,2,1,-10, 9, -90, 20])))
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

#hex, id, input, int, len, list, max, min, oct, open, range, pow, str, tuple, type,

#isinstance
class Person:
    pass
a = Person()
print(isinstance(a, Person))

#map
    #map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
    #map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
def pow(x):
    return x**2
print(list(map(pow, [1,2,3,4,5,6,7])))

#ord
    #returns ascii code for char
print(ord('a'))

#round
print(round(5.98361, 3))

#sorted
    #does not change value
a = [4,2,8,1,98,2,6,2,10]
print(sorted(a))
print(a)
    #does change value
a.sort()
print(a)

#sum
print(sum(a))

#zip
    #makes a list of tuples
b = list(zip(a, a))
print(b)
print(type(b[0]))
