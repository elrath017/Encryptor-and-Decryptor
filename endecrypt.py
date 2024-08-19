from nltk.tokenize import word_tokenize


# x = '''hello world
#  i am the hunter
#    welcome to the world
#      vengenance will be mine
#        i am justice'''

word_to_int = {}
lines = []  # Initialize lines variable

def encrypt_text(x):
    global lines  # Use global keyword to update the global lines variable
    lines = x.split('\n')  # Update the lines variable

    tokens = word_tokenize(x)

    word_freq = {}
    for word in tokens:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    for word in word_freq:
        if word not in word_to_int:
            word_to_int[word] = len(word_to_int)

    # Encrypt the text by replacing each word with its corresponding integer
    #encrypted_text = [str(word_to_int[word]) for word in tokens]
    encrypted_text = ""
    for line in lines:
        line_tokens = word_tokenize(line)
        for token in line_tokens:
            encrypted_text += str(word_to_int[token])
            if token != line_tokens[len(line_tokens)-1]:
                encrypted_text += " "
        if line != lines[len(lines)-1]:
            encrypted_text += "\n"

    return encrypted_text
    # print('Encrypted text:')
    # print(' '.join(encrypted_text))

#encrypt_text(x)

# Create a dictionary that maps each integer to its corresponding word
int_to_word = {v: k for k, v in word_to_int.items()}

def decrypt_text(x):
    global lines  # Use global keyword to access the global lines variable
    decrypted_lines = []
    for line in lines:
        decrypted_tokens = []
        line_tokens = word_tokenize(line)
        for token in line_tokens:
            if token.isdigit():  # Check if the token is a valid integer
                decrypted_tokens.append(int_to_word[int(token)])
            else:
                decrypted_tokens.append(token)  # Append the non-encrypted word directly
        decrypted_line = ' '.join(decrypted_tokens)
        decrypted_lines.append(decrypted_line)

    # Join the decrypted lines into a single string
    decrypted_text = '\n'.join(decrypted_lines)
    # print('\nDecrypted text:')
    # print(decrypted_text)
    return decrypted_text

#decrypt_text(x)
