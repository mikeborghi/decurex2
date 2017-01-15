import json
import os
import random
import unittest

import bitcoin.ripemd as ripemd
from bitcoin import *



# private key
pv_key1 = b'64ADAF4EECC5BA2E59A10A20770657D869AE1AF842BCC1A11ACFE1820ED33C9F'
# public key from that private key
pubkey1 = privkey_to_pubkey(pv_key1)

# private key
pv_key2 = b'5KdttCmkLPPLN4oDet53FBdPxp4N1DWoGCiigd3ES9Wuknhm8uT'
# public key from that private key
pubkey2 = privkey_to_pubkey(pv_key2)

print(pubkey1 + " ---> uncompressed")
pubkeyc = compress(pubkey1)
print(pubkeyc + " ---> compressed")

# address from compressed pub key
addr = pubkey_to_address(pubkeyc)
print(addr)

# find address unspent outputs
h = history(addr)
print(h)
# set outs to the output [value, address to send]
outs = [{'value': 90000, 'address': '16iw1MQ1sy1DtRPYw3ao1bCamoyBJtRB4t'}]

tx = b'010000000248a350154acf77320793b4385e52a6a78ca30b6dc4deee198845b52a3de0e5c7010000008a473044022022ea70cb558f683596b9567c40bee81a768fd828576581a98083d4e75fb8da1f02207b5637c8049551f07706b6befdb928ebb531270ef7042e8b4158c164cabbde34014104631b00474f81107010f8a385349a8bf722ec6c5ae2dc2bd397a6f8580eab48ad37325fdc93d1311ddf90f92817738a46328e885a571f197c159d49557a277ef9ffffffff48a350154acf77320793b4385e52a6a78ca30b6dc4deee198845b52a3de0e5c7000000006a473044022036d6d968496df5c57eb707517311582431dfa42f998bfdb973b38c09674e91b902203405e1faa9b7393e85e753a79853c738a6af191579110cea8f514763dc494eae0121028a771fd5c401ca6074d87a945afb6a8f346b2e5198a31b3cf450e92d0e29699fffffffff02d0b00b01000000001976a9149389139979aacd274609dba8ee72eb7159cc40ee88accfb00b01000000001976a914b4c3996ead2bf167525193a2f888b99fd7a76a6288ac00000000'

txd = deserialize(tx)
print(txd)

# scr = txd['outs'][0]['script']
# # txd['outs'][0]['script'] = 0x394324
# print(txd['outs'][0]['script'])
print(txd)
wow = deserialize_script(txd['outs'][0]['script'])
print(wow)
print("beginning test")
test = [118, 169, '3ec6c3ed8dfc3ceabcc1cbdb0c5aef4e2d02873c', 136, 172, 118]
test2 = serialize_script(wow)
print(test2)


def setup_script():
    scrTest = []
    OP_EQUALVERIFY = 0x76
    OP_CHECKSIG = 169
    # OP_DUP = 
    # OP_HASH160
    scrTest.append(OP_EQUALVERIFY)
    print(scrTest)
    print("fick")
    # scrTestS = serialize_script(scrTest)
    # print(scrTestS)
#     scrTest = []
#     op_if = 99
#     op_checkmultisig = 
#     op_else = 
#     op_checksigverify = 
#     op_hash160 = 
#     op_equal = 
#     op_endif = 
#     scrTest.append(op_if)
#     print(scrTest)
#     print("fick")


setup_script()


scrd = deserialize_script(scr)
scr2 = serialize_script(scrd)

print(scrd)
print(scr2)

# print(scrd[1])
print("\n")




if __name__ == '__main__':
    print("yo")

