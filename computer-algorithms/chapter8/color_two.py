from random import randint


def sortColor(list):
    head = 0
    tail = len(list)-1
    while head < tail:
        if list[head] is 'R':
            while list[tail] is not 'B':
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
    b=r=0
    for i in range(10):
        j = randint(0,100)
        if j%2 ==0 :
            list[i] = 'R'
            r+=1
        else:
            list[i] = 'B'
            b+=1
    # list = ['B', 'R', 'B', 'B', 'B', 'B', 'R', 'B', 'B', 'R']
    print(b, r)
    print(list)
    sortColor(list)
    # print(list)

