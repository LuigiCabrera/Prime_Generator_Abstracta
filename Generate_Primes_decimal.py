from miller_rabin_module import miller_rabin_test
from time import time
from math import log10
import random
random.seed(time())

#Genera el minimo impar de d digitos
def generate_prime_candidate(d, min=False):
    n = 10 ** (d-1)
    if d > 1: n += 1 
    return n

def generate_prime(b):
    if b == 1: return None
    n = generate_prime_candidate(b)
    while miller_rabin_test(n,128): n = n+2
    return n

def find_primes(digits, limit):
    if digits == 1: return [2,3,5,7]
    primes = []
    for i in range(generate_prime_candidate(digits), generate_prime_candidate(digits+1)-1, 2):
        if len(primes) == limit: break
        if not miller_rabin_test(i, max(int(log10(i)), 20)): primes.append(i)
    return primes

def main():
    print("\n\n\t\t ** Find primes with especific decimal lenght **\n\n")
    while True:
        b = int(input("Numero de digitos: "))
        if b == 0: break
        l = int(input("Limite de numeros a encontrar: "))
        primes = find_primes(b,l)
        print(f"\n{len(primes)} Primos encontrados (digits = {b}, limit = {l}):")
        for i in primes: print(i,end="\t")
        print("\n")
main()