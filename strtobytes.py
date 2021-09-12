import binascii
import base64


string = input("Enter the string:")

res = bytes(string, 'utf-8')
res1 = binascii.b2a_hex(res)



res2 = base64.b64encode(res1)

print(res2)

