 for char in text: 
        if 'a' <= char <= 'z':
            if 'a' <= char <= 'm':
                new_char = ord(char) + (n * m)
                new_char = (new_char - ord('a')) % 26 + ord('a')
        else:
            new_char = ord(char) + (n + m)
            new_char = (new_char - ord('a')) % 26 + ord('a')
