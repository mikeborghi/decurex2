import json
import os
import random
import unittest

import bitcoin.ripemd as ripemd
from bitcoin import *



# private key
pv_key1 = b'64ADAF4EECC5BA2E59A10A20770657D869AE1AF842BCC1A11ACFE1820ED33C9F'
# public key from that private key
pvkey1t = decode_privkey(pv_key1)
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
print(h[0])
input_tx1 = {'output': u'aabc3948a8f2fe4744314d92649857787f87614a83b7ba273f0daf9ce62c1e49:0', 'block_height': 448265, 'value': 10000, 'address': u'1K4BfG6qZF2BkV2v721mpBqAKDB3J63Y3y'}
# set outs to the output [value, address to send]
# outs = [{'value': 90000, 'address': '16iw1MQ1sy1DtRPYw3ao1bCamoyBJtRB4t'}]


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
print("this is redeemscript1")
print(red_tx1)
print("\n")
hred = hash160(red_tx1)
print(hred)

# sets up scriptpubkey for tx1
def setup_scripttx1():
    scrTest = []
    OP_HASH160 = 0xa9
    OP_EQUAL = 0x87
    scrTest.append(OP_HASH160)
    scrTest.append(hred)
    scrTest.append(OP_EQUAL)
    
    print(scrTest)
    
    scriptpubkey = serialize_script(scrTest)
    return scriptpubkey
scriptpubkey_tx1 = setup_scripttx1()

test2 = deserialize_script(scriptpubkey_tx1)
print(scriptpubkey_tx1)
print("fuckkk")
addrscr = script_to_address(scriptpubkey_tx1)
# addrscr = p2sh_scriptaddr(scriptpubkey_tx1)
print(addrscr)
# creates an output for tx1
tx1value = 100000
output_tx1 = {'value': tx1value,'address':addrscr,'scriptPubKey':test2}


print("WOW DAWHG")
print([output_tx1])
tx = mktx(h,[output_tx1])
print(tx)
txd = deserialize(tx)
print(txd)

# ready to use tx1
txnew = sign(tx,0,pv_key1)
print(txnew)

txnewer = deserialize(txnew)
print(txnewer)




def setup_scriptsig_tx2():
    scrTest = []
    OP_IF = 0x63
    OP_CHECKMULTISIG = 0xae
    OP_ELSE = 0x67
    OP_HASH160 = 0xa9
    OP_TRUE = 0x51
    # OP_EQUAL = 0x87
    

    scrTest.append('00')
    scrTest.append(pubkeyc)
    scrTest.append(pubkeyc2)
    scrTest.append(OP_TRUE)
    scrTest.append(red_tx1)
   
    
    print(scrTest)
    
    scriptPubKey2 = serialize_script(scrTest)
    return scriptPubKey2
    print("fick")
realscriptpubkey = setup_scriptsig_tx2()
# OP_DUP OP_HASH160 script OP_EQUALVERIFY OP_CHECKSIG
def scriptpubkey_2():
    scrTest = []
    OP_HASH160 = 0xa9
    OP_DUP = 0x76
    OP_EQUALVERIFY = 0x88
    OP_CHECKSIG = 0xac
    
    scrTest.append(OP_DUP)
    scrTest.append(OP_HASH160)
    scrTest.append(hash160(pubkey1))
    scrTest.append(OP_EQUALVERIFY)
    scrTest.append(OP_CHECKSIG)
    
    scriptpubkey_tx2 = serialize_script(scrTest)
    
    return scriptpubkey_tx2
    
scriptPubKey_tx2t = scriptpubkey_2()
output_tx2 = {'value': 100000, 'address':addrscr, 'scriptPubKey': scriptPubKey_tx2t  }

input_tx2 = { txnewer['ins'][0]['outpoint']['hash'] }

tx2 = mktx([input_tx1],[output_tx2])
print(tx2)
tx2_des = deserialize(tx2)
print(tx2_des)
# time to sign!
tx2new = sign(tx2,0,pv_key1)
print(tx2new)
# setup_script()



# print(scrd[1])





if __name__ == '__main__':
    print("yo")

