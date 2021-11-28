from miller_rabin_module import miller_rabin_test
from math import log10

def main():
    print("\n\n\t\t*** MILLER-RABIN PRIMALTY TEST **\n\n")
    while True:
        x = int(input("Ingrese x (Comprobar primalidad): "))
        if x == 0: break
        r = miller_rabin_test(x,max(int(log10(x)), 20))
        if r == None: print("Input invalido")
        elif not r: print('MUY PROBABLEMENTE PRIMO')
        else: print("No es primo :(")
        print("")
    
main()