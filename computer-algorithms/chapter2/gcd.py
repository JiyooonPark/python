def gcd(a,b):
    while b>0:
        r = a%b
        a = b
        b = r
    return a

def gcd_rec(a, b):
    if b <= 0:
        return a
    else:
        return gcd(b, a%b)

def gcd2(a, b):
    while a != b:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a

def gcd2_rec(a, b):
    if a==b:
        return a
    else:
        if a>b:
            return gcd2_rec(a-b, b)
        else:
            return gcd2_rec(a, b-a)


print( gcd(600, 54))
print( gcd_rec(600, 54))
print( gcd2(100, 54))
print( gcd2_rec(100, 54))