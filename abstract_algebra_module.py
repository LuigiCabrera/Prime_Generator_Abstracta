def gcd(a,b):
    if a % b == 0: return b
    return gcd(b, a%b)

def expomod(x, y, p):
    res = 1
    x = x % p
    if x == 0: return 0
    while y > 0:
        if (y & 1) == 1: res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def gcd_ext(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = gcd_ext(b % a, a)
        return g, x - (b // a) * y, y

def inverso_mult(a, m):
    g, x, y = gcd_ext(a, m)
    if g != 1:
        return None
    else:
        return x % m