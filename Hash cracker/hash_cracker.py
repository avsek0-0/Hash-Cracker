import hashlib
import pyfiglet

print (pyfiglet.figlet_format("HASH CRACKER"))

print ("Algorithm available: MD5 | SHA1 | SHA224 | SHA256 | SHA512 | SHA384 \n")

hash_type = str (input("Specify The Hash Type: "))
hash_type = hash_type.upper()
wordlist_location = str ( input ("\nEnter the wordlist location: "))
hash = str(input("\nEnter the hash: "))

if (hash_type==""):
    print ("Please specify the Hash Type !!")
    exit()
elif (wordlist_location==""):
    print ("Please specify the Wordlist Location !!")
    exit()
elif (hash==""):
    print("Please Specify the Hash !!")
    exit()



try:                                                            # handling the unidentified wordlist
    f = open (f"{wordlist_location}","r",encoding="latin-1")
except FileNotFoundError:
    print ("\nPlease specify correct file location !!")
    exit()
else:
    for password in f:
        password = password.strip().encode('latin-1')

        if hash_type == "MD5":
            hash_object = hashlib.md5 (password)
            hashed = hash_object.hexdigest()
            if hash == hashed:
                print ("HASH FOUND: {} \n".format(password.decode('latin-1')))
                exit()
        
        elif hash_type == "SHA1":
            hash_object = hashlib.sha1 (password)
            hashed = hash_object.hexdigest()
            if hash == hashed:
                print ("HASH FOUND: {} \n".format(password.decode('latin-1')))
                exit()

        elif hash_type == "SHA224":
            hash_object = hashlib.sha224 (password)
            hashed = hash_object.hexdigest()
            if hash == hashed:
                print ("HASH FOUND: {} \n".format(password.decode('latin-1')))
                exit()

        elif hash_type == "SHA256":
            hash_object = hashlib.sha256 (password)
            hashed = hash_object.hexdigest()
            if hash == hashed:
                print ("HASH FOUND: {} \n".format(password.decode('latin-1')))
                exit()

        elif hash_type == "SHA512":
            hash_object = hashlib.sha512 (password)
            hashed = hash_object.hexdigest()
            if hash == hashed:
                print ("HASH FOUND: {} \n".format(password.decode('latin-1')))
                exit()

        elif hash_type == "SHA384":
            hash_object = hashlib.sha384 (password)
            hashed = hash_object.hexdigest()
            if hash == hashed:
                print ("\nHASH FOUND: {} ".format(password.decode('latin-1')))
                exit()

        else:
            print ("Choose the correct \'Hash Type\' from the given options !! ")
            break



