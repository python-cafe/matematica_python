

def mdc_iterativo(a, b):
    if a < b:
        a, b = b, a

    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

def mdc(a, b):
    if a < b:
        return mdc(b, a)
    if b == 0:
        return a
    r = a % b
    return mdc(b, r)
