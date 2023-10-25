import base64
import binascii

def AWSAccount_from_AWSKeyID(AWSKeyID):
    
    trimmed_AWSKeyID = AWSKeyID[4:] #remove KeyID prefix
    x = base64.b32decode(trimmed_AWSKeyID) #base32 decode
    y = x[0:6]
    
    z = int.from_bytes(y, byteorder='big', signed=False)
    mask = int.from_bytes(binascii.unhexlify(b'7fffffffff10'), byteorder='big', signed=False)
    
    e = (z & mask)>>7
    return (e)


print ("account id:" + str(AWSAccount_from_AWSKeyID("ASIAY34FZKBOKMUTVV7A")))