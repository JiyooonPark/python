
# multiplication

def mult(a, b):
    if b == 1:
        return a
    else:
        return a+mult(a, b-1)
def div(a, b):
    if a < b:
        return 0
    else:
        return 1+div(a-b, b)
def mod(a, b):
    if a <b:
        return a
    else:
        return mod(a-b, b)
print("result is", str(mult(4, 10)))
print("result is", str(div(40, 10)))
print("result is", str(mod(42, 10)))