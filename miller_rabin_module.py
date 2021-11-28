import random
from time import time
random.seed(time())

def expomod(x, y, p):
    res, x = 1, x % p
    if x == 0: return 0
    while y > 0:
        if (y & 1) == 1: res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def witness(a, n, t, u):
    xi = expomod(a, u, n)
    if xi == 1 or xi == n-1: return False # PROBABLEMENTE PRIMO
    for i in range(1,t):
        xi = (xi*xi) % n
        if xi == n-1: return False # PROBABLEMENTE PRIMO
    return True # COMPUESTO

# n es compuesto?
def miller_rabin_test(n, s=1000):
    if n < 2: return None
    if n == 2: return False # 2 es primo
    if n % 2 == 0: return True # Numero mayor a 2 par siempre es compuesto

    # Escribir n − 1 como 2^t * u
    pow_2, t = 2, 1
    while (n-1) % pow_2 != 0 or ((n-1) // pow_2) % 2 == 0:
        pow_2 *= 2
        t+=1
    else: u = (n-1) // pow_2

    # Comprobar debilidades
    for i in range(s):
        if witness(random.randint(1, n-1),n,t,u): return True # Compuesto
    return False # PROBABLEMENTE PRIMO