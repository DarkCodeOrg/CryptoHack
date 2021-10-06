from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long, inverse
import math
from gmpy2 import next_prime

FLAG = b"crypto{????????????????????????????????????????????????}"

p = getPrime(1024)
q = getPrime(1024)
N = p*q
phi = (p-1)*(q-1)
e = 0x10001
d = inverse(e, phi)

my_key = (N, d)

friends = 5
friend_keys = [(N, getPrime(17)) for _ in range(friends)]

cipher = bytes_to_long(FLAG)

for key in friend_keys:
    cipher = pow(cipher, key[1], key[0])

print(f"My private key: {my_key}")
print(f"My Friend's public keys: {friend_keys}")
print(f"Encrypted flag: {cipher}")
