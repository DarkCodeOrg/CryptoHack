from pwn import xor

out = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526220f27342e175d0e077e263451150104')

flag_part = b'crypto{'



###
#key = xor(flag_part,out)
#
#
#print(key)


key = b'myXORkey'

print(xor(key,out))
                    

