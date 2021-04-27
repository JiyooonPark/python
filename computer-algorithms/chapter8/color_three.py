from random import randint


def sortColor(list):
    head = 0
    tail = len(list)-1
    while head < tail:
        if list[head] is not 0:
            while list[tail] is not 0:
                tail-=1
            print(head, tail)
            print("switch")
            if head>tail:
                break
            list[head], list[tail] = list[tail], list[head]
            print(list)
            # tail-=1
        head +=1
    head = 0
    tail = len(list)-1
    while list[head] is 0:
        head +=1
    while head < tail:
        if list[head] is not 1:
            while list[tail] is not 1:
                tail-=1
            print(head, tail)
            print("switch")
            if head>tail:
                break
            list[head], list[tail] = list[tail], list[head]
            print(list)
            # tail-=1
        head +=1
    print(list)


if __name__=="__main__":
    list = [None for i in range(10)]
    for i in range(10):
        j = randint(0,100)
        if j%3 ==0 :
            list[i] = 1
        elif j%2 ==0:
            list[i] = 0
        else:
            list[i] = 2
    # list = [0,1,2,1,1,2,0,1,2,1]
    print(list)
    sortColor(list)
    # print(list)

