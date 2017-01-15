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
def setup_script():
    scrTest = []
    OP_IF = 0x63
    OP_CHECKMULTISIG = 0xae
    OP_ELSE = 0x67
    OP_HASH160 = 0xa9
    OP_CHECKSIGVERIFY = 0xad
    OP_EQUAL = 0x87
    OP_ENDIF = 0x68
    scrTest.append(OP_IF)
    scrTest.append('02')
    scrTest.append(pubkeyc)
    scrTest.append(pubkeyc2)
    scrTest.append('02')
    scrTest.append(OP_CHECKMULTISIG)
    scrTest.append(OP_ELSE)
    scrTest.append(pubkeyc2)
    scrTest.append(OP_CHECKSIGVERIFY)
    scrTest.append(OP_HASH160)
    scrTest.append(hranx)
    scrTest.append(OP_EQUAL)
    scrTest.append(OP_ENDIF)
    
    print(scrTest)
    
    goodtx = serialize_script(scrTest)
    return goodtx
    print("fick")
script_tx1 = setup_script()
print("this is tx1")
print(script_tx1)
print("\n")

txt = deserialize_script(script_tx1)
print(txt)
# OP_IF 2 #{pubkey_a} #{pubkey_b} 2 OP_CHECKMULTISIG OP_ELSE #{pubkey_b} OP_CHECKSIGVERIFY 
# OP_HASH160 #{Digest::RMD160.hexdigest(Digest::SHA256.digest(x))} OP_EQUAL OP_ENDIF
# def setup_script():



# setup_script()



# print(scrd[1])
print("\n")




if __name__ == '__main__':
    print("yo")

