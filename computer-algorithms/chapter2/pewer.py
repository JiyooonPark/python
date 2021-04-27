def inter_power(x, n):
    result = 1
    for i in range(n):
        result*=x
    return result
def recur_power(x, n):
    if n is 1:
        return x
    else:
        return x*recur_power(x, n-1)
def bi_recur_power(x, n):
    if n == 0:
        print(0)
        return 1
    elif n%2 is 0:
        return bi_recur_power(x*x, n/2)
    else:
        return x * bi_recur_power(x*x, n//2)
print(bi_recur_power(2, 7))