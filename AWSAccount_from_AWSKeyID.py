import base64
import binascii

def AWSAccount_from_AWSKeyID(AWSKeyID):
    
    trimmed_AWSKeyID = AWSKeyID[4:] #remove KeyID prefix
    x = base64.b32decode(trimmed_AWSKeyID) #base32 decode
    y = x[0:6]
    
    z = int.from_bytes(y, byteorder='big', signed=False)
    mask = (int.from_bytes(binascii.unhexlify(b'ffffffffff00'), byteorder='big', signed=False))>>1 # 5 bytes mask, shifted by 1 bit

    e = (z & mask)>>7 # applying the mask, and shifting to remove x[6]'s 7 irrelevant bits
    return (e)


print ("account id:" + "{:012d}".format(AWSAccount_from_AWSKeyID("ASIAQNZGKIQY56JQ7WML")))
