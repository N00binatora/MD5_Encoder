import hashlib


#simple script to encrypt whatever the user types
fa = input("Enter string you wish to encrypt with MD5: ")
yarp = hashlib.md5(fa.encode())
print(yarp.hexdigest())
