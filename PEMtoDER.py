from OpenSSL import crypto


with open("privacy_enhanced_mail.pem","rb") as keyfile:
    cert_file = keyfile.read()
    cert_pem = crypto.load_certificate(crypto.FILETYPE_PEM, cert_file)
    cert_der = crypto.dump_certificate(crypto.FILETYPE_ASN1, cert_pem)

