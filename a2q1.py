file = open("raw_text.txt", "r")

def encrypt(text, n, m):
    encrypted_text = ""

    for char in text: 
        if 'a' <= char <= 'z':
            if 'a' <= char <= 'm':
                encrypted_char = chr(((ord(char) - ord('a') + n * m) % 26) + ord('a'))

            else: 
                encrypted_char = chr(((ord(char) - ord('a') - (n + m)) % 26) + ord('a'))

        elif 'A' <= char <= 'Z':
            if 'A' <= char <= 'M':
                encrypted_char = chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
            else: 
                encrypted_char = chr(((ord(char) - ord('A') + m ** 2) % 26) + ord('A'))       

                





