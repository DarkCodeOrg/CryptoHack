#!/usr/bin/env python3


import base64
import binascii
from binascii import unhexlify

def hexToAscii(hexx):
    asci = ""

    for i in range (0, len(hexx), 2):

        part = hexx[i : i + 2]
        ch = chr(int(part,16))

        asci += ch

    return asci

if __name__ == "__main__":
    hexxy = input("Enter hex string:")
    print("Ascii text is:",hexToAscii(hexxy))
    print("Bytes are :",bytes.fromhex(hexxy))
    print("Base64 is :",base64.b64encode(bytes.fromhex(hexxy)))
##	print("ASCII text is:", unhexlify(hexxy))



