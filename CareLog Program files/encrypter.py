"""
XOR Encryption with repeating key
then using Base64 to encode for readability
"""
import base64 # import base 64 to make the output readable and neat 

encryption_key = "CareLogHealthSystemByRithvikSufyaanHanjiAndAlex"

#encrpytion function, making sure the input and ouput of the function is a string
def encrypt(text: str) -> str:
    
    #Start with a empty string
    encrypted_message = "" 

    # Go through each character in the text with its index
    # Enumerate puts a index with each item it iterates over
    for i, char in enumerate(text):
        
        # Pick the matching character from the key (repeats when shorter)
        key_char = encryption_key[i % len(encryption_key)]
        
        # Turn the message code AND key code into their ASCII Numbers (a becomes 96, A becomes 65 etc.)
        message_code = ord(char)
        key_code = ord(key_char)
        
        # XOR the two numbers (for XOR encryption)
        encrypted_code = message_code ^ key_code
        
        # Turn the numerical binary result into a character
        encrypted_char = chr(encrypted_code)
        
        # Add that character into the string of the encrypted message
        encrypted_message += encrypted_char
    
    #returns the encrypted message into a bunch of symbols, characters, numbers (for easier reading) using base64
    # (basically encoding the encrypted message with base64)
    return base64.b64encode(encrypted_message.encode()).decode()


#encryption function but reversed
def decrypt(text: str) -> str:
    
    decrypted_message = ""
    
    #turn from the base64 encoded message into the basic encrypted message by decoding it with base64
    decoded_message = base64.b64decode(text).decode()
    
    # same thing as encrypt 
    for i, char in enumerate(decoded_message):
        key_char = encryption_key[i % len(encryption_key)]
        
        #same thing
        message_code = ord(char)
        key_code = ord(key_char)
        
        #same thing but reversed
        decrypted_code = message_code ^ key_code
        
        decrypted_char = chr(decrypted_code)
        
        decrypted_message += decrypted_char
        
    return decrypted_message
    
if __name__=="__main__":
    msg = "LB33"
    enc = encrypt(msg)
    dec = decrypt(enc)
    print("Encrypted:", enc)
    print("Decrrypted:", dec)


"""
references: https://docs.python.org/3/library/base64.html
https://www.tutorialspoint.com/cryptography/cryptography_xor_encryption.htm?utm_source=chatgpt.com 
https://www.tutorialspoint.com/cryptography/cryptography_base64_encoding_and_decoding.htm
"""