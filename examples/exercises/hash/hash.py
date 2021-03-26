
# What is hashing?


import hashlib
from binascii import hexlify

data = 'Sending Encrypted'
data = data.encode('utf-8')

sha3_512 = hashlib.sha3_512(data)
sha3_512_digest = sha3_512.digest()
sha3_512_hex_digest = sha3_512.hexdigest()

print('Printing digest output')
print(sha3_512_digest)
print('Printing hex output')
print(sha3_512_hex_digest)
print('Printing binary hex')
print(hexlify(sha3_512_digest))


