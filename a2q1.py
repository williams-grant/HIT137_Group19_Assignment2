file = open("raw_text.txt", "r")
def encrypt(text, n, m):
    encrypted_text = ""

# Don't use char as variable name as char is also a function you will need to use
# Can use something like char_to_encrypt
for char_to_encrypt in text: 
        # If you structure your if statements like this, then you don't need to nest them.
        # if 'a' <= char <= 'm':
        # elif 'n' <= char <= 'z':
        # elif 'A' <= char <= 'M':
        # elif 'N' <= char <= 'Z':
        # else:
        #    new_char = char
        # Note: else is required because non-letter characters need to be retained e.g. spaces, full stops etc
        if 'a' <= char_to_encrypt <= 'z':
            if 'a' <= char <= 'm':
                new_char = char(ord(a) + ord(char_to_encrypt) - ord(a) + (n * m) ) % 26)
                # This one can be done with one line: new_char = char(ord(a) + (ord(char_to_encrypt) - ord(a) + (n * m)) % 26)
        else:
            new_char = ord(char_to_encrypt) + (n + m) 
            new_char = (new_char - ord('a')) % 26 + ord('a')
            # This one needs to shift backwards and there are two scenarios:
            # 1) The shift back stays within the range of a-z
            #        can be tested by ord(char_to_encrypt) - ord(a) - ((n + m) % 26) >= 0
            #        then calculated as new_char = char(ord(char_to_encrypt) - ((n + m) % 26))
            # 2) The shift back goes below the range of a-z (this would be the else to the above test)
            #        then calculated as new_char = char(ord(char_to_encrypt) + 26 - ((n + m) % 26))

        
