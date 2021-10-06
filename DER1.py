from Crypto.PublicKey import RSA
## the der file has been atfirst converted into pem file using the below command 
## openssl x509 -inform DER -outform PEM -in 2048b-rsa-example-cert.der -out 2048b-rsa-example-cert.pem
with open('2048b-rsa-example-cert.pem','r') as key_file:
    key = RSA.import_key(key_file.read())
    print(type(key))
    print(key.n)
