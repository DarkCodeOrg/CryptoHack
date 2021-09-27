#!/usr/bin/env python3


from Crypto.Util.number import getPrime, bytes_to_long, inverse
from random import getrandbits
from math import gcd

FLAG = b"crypto{?????????????????????????}"

m = bytes_to_long(FLAG)

def get_huge_RSA():
    p = getPrime(1024)
    q = getPrime(1024)
    N = p*q
    phi = (p-1)*(q-1)
    while True:
        e = getrandbits(2048)
        if gcd(e,phi) == 1:
            break
    return N,e


N, e = get_huge_RSA()
c = pow(m, e, N)

print(f'N = {hex(N)}')
print(f'e = {hex(e)}')
print(f'c = {hex(c)}')
