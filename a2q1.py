file = open("raw_text.txt", "r")
def encrypt(text, n, m):
    encrypted_text = ""

for char in text: 
        if 'a' <= char <= 'z':
            if 'a' <= char <= 'm':
                new_char = ord(char) + (n * m)
                new_char = (new_char - ord('a')) % 26 + ord('a')
        else:
            new_char = ord(char) + (n + m)
            new_char = (new_char - ord('a')) % 26 + ord('a')
