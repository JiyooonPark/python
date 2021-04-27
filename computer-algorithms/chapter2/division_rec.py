
def rec_division(a, b):
    # have to return a/b, a%b
    if a<b:
        return [0, a]
    else:
        return [1+rec_division(a-b, b)[0], rec_division(a-b, b)[1]]

print(rec_division(90,4))