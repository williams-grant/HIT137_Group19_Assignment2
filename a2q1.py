def encrypt(text, n, m):
    encrypted_text = ""
    
    for char_to_encrypt in text:
        if 'a' <= char_to_encrypt <= 'm':
            new_char = chr(ord('a') + (ord(char_to_encrypt) - ord('a') + (n * m)) % 26)
        elif 'n' <= char_to_encrypt <= 'z': 
            new_char = chr(ord('a') + (ord(char_to_encrypt) - ord('a') - (n + m)) % 26)
        elif 'A' <= char_to_encrypt <= 'M':  
            new_char = chr(ord('A') + (ord(char_to_encrypt) - ord('A') - n) % 26)
        elif 'N' <= char_to_encrypt <= 'Z':  
            new_char = chr(ord('A') + (ord(char_to_encrypt) - ord('A') + (m**2)) % 26)    
        else:
            new_char = char_to_encrypt

    encrypted_text += new_char
    return encrypted_text

def decrypt(text, n, m):
    decrypted_text = ""
    for char_to_decrypt in text:
        if 'a' <= char_to_decrypt <= 'm':
            new_char = chr(ord('a') + (ord(char_to_decrypt) - ord('a') - (n * m)) % 26)
        elif 'n' <= char_to_decrypt <= 'z': 
            new_char = chr(ord('a') + (ord(char_to_encrypt) - ord('a') + (n + m)) % 26)
        elif 'A' <= char_to_decrypt <= 'M':  
            new_char = chr(ord('A') + (ord(char_to_decrypt) - ord('A') + n) % 26)
        elif 'N' <= char_to_decrypt <= 'Z':  
            new_char = chr(ord('A') + (ord(char_to_decrypt) - ord('A') - (m**2)) % 26)    
        else:
            new_char = char_to_decrypt

    decrypted_text += new_char
    return decrypted_text


def main():
    with open("raw_text.txt", "r") as file:
        original_text = file.read()

n = int(input("enter the value for n: "))
m = int(input("Enter the value for m: "))
