# Import Fernet from fernet of the cryptography module
from cryptography.fernet import Fernet
#Getting the value of the key using the generate_key() function
keyvalue = Fernet.generate_key()
#Getting the fernet object by passing the above key value to the Fernet function
Fernet_object= Fernet(keyvalue)
#Pass some random string by adding b as prefix to it for the encrypt function of the above fernet object 
#Here we get encrypted text
Encrypted_text = Fernet_object.encrypt(b"Hello Good morning this is BTechgeeks ")
#Getting the original Text using the decrypt function of the above fernet object 
Original_text= Fernet_object.decrypt(Encrypted_text)
print("The Encrypted Text of the Above String is:\n\n", Encrypted_text)
print("\nThe Original Text (Decrypted text) of the above string is:\n\n",Original_text)
