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
pubkeyc = compress(pubkey1)

print(pubkeyc + " ---> compressed 1")
# private key
pv_key2 = b'5KdttCmkLPPLN4oDet53FBdPxp4N1DWoGCiigd3ES9Wuknhm8uT'
# public key from that private key
pubkey2 = privkey_to_pubkey(pv_key2)
pubkeyc2 = compress(pubkey2)
print(pubkeyc2 + " ---> compressed 2")



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

scr = txd['outs'][0]['script']
# txd['outs'][0]['script'] = 0x394324
print(txd)


print("\n \n \n")
# The random number thats not so random right now
ranx = '9439429'
hranx = hash160(ranx)
print(hranx)
# this script sets up an output which consume the entire value of the input.  you would need to create a separate output for change, just put it in an array
def setup_redeemtx1():
    scrTest = []
    OP_IF = 0x63
    OP_CHECKMULTISIG = 0xae
    OP_ELSE = 0x67
    OP_HASH160 = 0xa9
    # OP_CHECKSIGVERIFY = 0xad
    # OP_EQUAL = 0x87
    OP_ENDIF = 0x68
    OP_EQUALVERIFY = 0x88
    OP_CHECKSIG = 0xac
    scrTest.append(OP_IF)
    scrTest.append('02')
    scrTest.append(pubkeyc)
    scrTest.append(pubkeyc2)
    scrTest.append('02')
    scrTest.append(OP_CHECKMULTISIG)
    scrTest.append(OP_ELSE)
    scrTest.append(OP_HASH160)
    scrTest.append(hranx)
    scrTest.append(OP_EQUALVERIFY)
    scrTest.append(pubkeyc2)
    scrTest.append(OP_CHECKSIG)
    scrTest.append(OP_ENDIF)
    
    print(scrTest)
    
    redeem = serialize_script(scrTest)
    return redeem
    print("fick")
red_tx1 = setup_redeemtx1()
print("this is tx1")
print(red_tx1)
print("\n")
hred = hash160(red_tx1)
print(hred)

def setup_scripttx1():
    scrTest = []
    OP_HASH160 = 0xa9
    OP_ENDIF = 0x68
    scrTest.append(OP_HASH160)
    scrTest.append(hred)
    scrTest.append(OP_ENDIF)
    
    print(scrTest)
    
    scriptpubkey = serialize_script(scrTest)
    return scriptpubkey
scriptpubkey_tx1 = setup_scripttx1()
print(scriptpubkey_tx1)
print("fuckkk")

# txt = deserialize_script(red_tx1)
# print(txt)




# setup_script()



# print(scrd[1])
print("\n")




if __name__ == '__main__':
    print("yo")

