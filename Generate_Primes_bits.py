from miller_rabin_module import miller_rabin_test
from time import time
from math import log10
import random
random.seed(time())

#Genera el minimo impar de b bits o un impar aleatorio de b bits
def generate_prime_candidate(b, min=False):
    if b == 1: return 1
    if b == 2: return random.randint(2,3)
    n = 1
    for i in range(b-2): 
        n = (n << 1)
        if not min: n = n | random.randint(0,1)
    return (n << 1) | 1

def generate_prime(b):
    if b == 1: return None
    n = generate_prime_candidate(b)
    while miller_rabin_test(n,128): n = n+2
    return n

def find_primes(bits, limit):
    primes = []
    for i in range(generate_prime_candidate(bits, True), generate_prime_candidate(bits+1, True)-1, 2):
        if len(primes) == limit: break
        if not miller_rabin_test(i, max(int(log10(i)), 20)): primes.append(i)
    return primes

def main():
    print("\n\n\t\t ** Find primes with especific bit lenght **\n\n")
    while True:
        b = int(input("Numero bits (b): "))
        if b == 0: break
        if b <= 2: continue
        l = int(input("Limite de numeros a encontrar: "))
        primes = find_primes(b,l)
        print(f"\n{len(primes)} Primos encontrados (bits = {b}, limit = {l}):")
        for i in primes: print(i,end="\t")
        print("\n")
main()