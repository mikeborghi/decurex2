import json
import os
import random
import unittest

import bitcoin.ripemd as ripemd
from bitcoin import *

# private key
pv_key1 = b'64ADAF4EECC5BA2E59A10A20770657D869AE1AF842BCC1A11ACFE1820ED33C9F'
# public key from that private key
pubkey = privkey_to_pubkey(pv_key1)

print(pubkey + " ---> uncompressed")
pubkeyc = compress(pubkey)
print(pubkeyc + " ---> compressed")
# address from compressed pub key
addr = pubkey_to_address(pubkeyc)
print(addr)
# find address unspent outputs
h = history(addr)
print(h)
# set outs to the output [value, address to send]
outs = [{'value': 90000, 'address': '16iw1MQ1sy1DtRPYw3ao1bCamoyBJtRB4t'}]
tx = mktx(h,outs)
print(tx)
txd = deserialize(tx)
print(txd)
print(txd['outs'][0]['script'])
scr = b'76a9143ec6c3ed8dfc3ceabcc1cbdb0c5aef4e2d02873c88ac'
scrd = deserialize_script(scr)
print(scrd)
print(scrd[1])
print("\n")




if __name__ == '__main__':
    print("yo")

