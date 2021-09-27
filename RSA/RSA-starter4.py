import sys
from typing import Tuple
sys.setrecursionlimit(1000000)  # long type, 32bit OS 4B, 64bit OS 8B (1bit for sign)

def egcd(a: int, b: int) -> Tuple[int, int, int]:
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    if a == 0:
        return (b, 0, 1)
    else:
        b_div_a, b_mod_a = divmod(b, a)
        g, x, y = egcd(b_mod_a, a)
        return (g, y - b_div_a * x, x)

def modinv(a: int, b: int) -> int:
    """return x such that (x * a) % b == 1"""
    g, x, _ = egcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b

print(modinv(65537,882564595536224140639625987657529300394956519977044270821168))


