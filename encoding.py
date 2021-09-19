from binascii import unhexlify
from pwn import *
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes
import json
import sys
import Crypto


r = remote('socket.cryptohack.org', 13377, level = 'debug')

class Decoder(object):
    def __init__(self,data):
        self.type = ''
        self.data = ''
        loaded_json = json.loads(data)
        self.type = loaded_json['type']
        self.data = loaded_json['encoded']

        print("recieved this %s,%s",self.data,self.type)

    def calling(self):

        if self.type == "base64":
            return base64.b64decode(self.data).decode('ISO-8859-1')

        elif self.type == "hex":
            return bytes.fromhex(self.data).decode('ISO-8859-1')

        elif self.type == "rot13":
            return codecs.decode(self.data, 'rot_13')
        
        elif self.type == "bigint":
            len_decode = len(self.data)
            x =  int(self.data, 16).to_bytes(len_decode, 'big')
            return str(x, 'UTF-8').lstrip('\x00')

        elif self.type == "utf-8":
            return  ''.join(chr(o) for o in self.data)
    
   
        
for i in range(100):
    retrieve = r.recv_raw(1024)
    decoder = Decoder(retrieve)
    decode = decoder.calling()
    print("decoded ==== %s %s",i,decode)
    decode = {
        "decoded": decode
    }
    response = json.dumps(decode)

    r.send(response)


print('\n\nthe flag is:'+r.recv(1024).decode('ISO-8859-1'))

