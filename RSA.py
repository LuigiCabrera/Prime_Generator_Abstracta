from miller_rabin_module import miller_rabin_test
from abstract_algebra_module import *
from time import time
from math import log10
import hashlib
import random

random.seed(time())

def generate_e():
    l = [3, 5, 17, 257, 65537]
    return l[random.randint(0,len(l)-1)]

def generate_prime_candidate(b): # (2^b) + 1 = 1000...0001
    if b == 1: return 1
    if b == 2: return random.randint(2,3)
    n = 1
    for i in range(b-1): n = (n << 1) | random.randint(0,1)
    return n | 1

def generate_primes_RSA(b,e):
    if b == 1: return None
    p = generate_prime_candidate(b)
    while miller_rabin_test(p, max(int(log10(p)), 128)) or p%e == 1: p += 2
    q = p+2
    while miller_rabin_test(q, max(int(log10(q)), 128)) or q%e == 1: q += 2
    return p,q

def RSA_key_generator(bits):
    e = generate_e()
    p, q = generate_primes_RSA(bits//2,e)
    euler = (p-1)*(q-1)
    d = inverso_mult(e, euler)
    return p*q, e, d

# Convierte mensaje (str) a bits y los bits a un entero para operarlo 
def string_bits_to_int(m):
    return int(''.join(format(ord(i), '08b') for i in m), 2)

def sign_verify(M, c, e, n):
    h = hashlib.sha1(M.encode()).hexdigest()
    if string_bits_to_int(h) == expomod(c, e, n): return True
    return False

def main():
    print("\n\n\t\t*** RSA KEY GENERATOR AND DIGITAL SIGN ***\n\n")
    while True:

        M = input("Ingrese un mensaje: ") # Mensaje
        if M == "": break

        n,e,d = RSA_key_generator(400)
        print(f"\nModule:\t{n}\nPublic Key: {e}\nPrivate Key: {d}\n")

        h = hashlib.sha1(M.encode()).hexdigest() # Hash
        c = expomod(string_bits_to_int(h), d, n) # Firma

        print("\nEnviar por canal inseguro:\nMensaje:", M,"\nC (Firma):",c,"\n")
        
        verify = sign_verify(M,c,e,n)
        if verify: print("La firma ha sido verificada exitosamente!\n")
        else: print("La firma no es valida!\n")

main()