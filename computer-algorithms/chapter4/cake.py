
def candle(n, k):
    left = n
    turn = k
    list = [0 for i in range(n)]
    for i in range(n):
        list[i] = 1

    while left is not 1:
        print(left, turn, list)
        list[turn] = 0
        i=0
        while i <= k:
            turn += 1
            turn %= n
            i+=1
            if list[turn]==0:
                i -=1
        turn %= n
        while(list[turn] is 0):
            turn += 1
            turn %= n
        left-=1
    print(list)
    for i in range(n):
        if list[i] is 1:
            return i

print(candle(7, 3))