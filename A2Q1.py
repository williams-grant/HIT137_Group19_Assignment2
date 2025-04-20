import os

def encrypt(original_text, n, m):
    encrypted_text = ''
    key_text = ''
    
    for char_to_encrypt in original_text:
        if 'a' <= char_to_encrypt <= 'm':
            new_char = chr(ord('a') + (ord(char_to_encrypt) - ord('a') + (n * m)) % 26)
            key_char = '1'
        elif 'n' <= char_to_encrypt <= 'z': 
            new_char = chr(ord('a') + (ord(char_to_encrypt) - ord('a') - (n + m)) % 26)
            key_char = '2'
        elif 'A' <= char_to_encrypt <= 'M':  
            new_char = chr(ord('A') + (ord(char_to_encrypt) - ord('A') - n) % 26)
            key_char = '3'
        elif 'N' <= char_to_encrypt <= 'Z':  
            new_char = chr(ord('A') + (ord(char_to_encrypt) - ord('A') + (m**2)) % 26) 
            key_char = '4'
        else:
            new_char = char_to_encrypt
            key_char = '0'
            
        encrypted_text += new_char
        key_text += key_char
    return encrypted_text, key_text

def decrypt(encrypted_text, key_text, n, m):
    decrypted_text = ''
    for char_pos in range(0, len(encrypted_text)):
        char_to_decrypt = encrypted_text[char_pos]
        key_char = key_text[char_pos]
        if key_char == '1':
            new_char = chr(ord('a') + (ord(char_to_decrypt) - ord('a') - (n * m)) % 26)
        elif key_char == '2': 
            new_char = chr(ord('a') + (ord(char_to_decrypt) - ord('a') + (n + m)) % 26)
        elif key_char == '3':  
            new_char = chr(ord('A') + (ord(char_to_decrypt) - ord('A') + n) % 26)
        elif key_char == '4':  
            new_char = chr(ord('A') + (ord(char_to_decrypt) - ord('A') - (m**2)) % 26)    
        else:
            new_char = char_to_decrypt
            
        decrypted_text += new_char
    return decrypted_text


def main():
    file_path = os.path.join(os.path.dirname(__file__), 'raw_text.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        original_text = file.read()
        
    m = int(input('Enter the value for m: '))
    n = int(input('Enter the value for n: '))
       
    encrypted_text, key_text = encrypt(original_text, m, n)

    encrypted_file_path = os.path.join(os.path.dirname(__file__)), 'encrypted_text.txt'
    with open((os.path.dirname(__file__) + 'encrypted_text.txt'), 'w', encoding='utf-8') as outfile:
        outfile.write(encrypted_text)
            
    decrypted_text = decrypt(encrypted_text, key_text, m, n)
    with open((os.path.dirname(__file__) + 'decrypted_text.txt'), 'w', encoding='utf-8') as outfile:
        outfile.write(decrypted_text)
    
    if original_text == decrypted_text:
        print('Encryption and decryption successful.')
    else:
        print('Decrypted text does not match original text. Encryption and decryption unsuccessful')

if __name__ == '__main__':
    main()
