# Caesar Cipher Program: A simple encryption and decryption implementation using a shift cipher.

# Defining a string of lowercase English letters to map characters
letters = 'abcdefghijklmnopqrstuvwxyz'
# Storing the number of letters in the alphabet
num_letters = len(letters)

# Function to encrypt or decrypt a given text using Caesar cipher


def encypt_decrypt(text, mode, key):
    result = ''  # Variable to store the final result after encryption or decryption

    # If mode is 'd' (decryption), reverse the key by making it negative
    if mode == 'd':
        key = -key

    # Iterate through each character in the input text
    for letter in text:
        letter = letter.lower()  # Convert the letter to lowercase for uniformity

        # Skip spaces as they don't need to be encrypted or decrypted
        if not letter == ' ':
            # Find the index of the letter in the alphabet string
            index = letters.find(letter)

            # If the letter is not found (i.e., not part of the alphabet), leave it unchanged
            if index == -1:
                result += letter
            else:
                # Calculate the new index after shifting by the key
                new_index = index + key

                # If the new index goes beyond the alphabet, wrap around using modulus
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters

                # Append the new letter at the new index to the result
                result += letters[new_index]

    return result


# Start of the program
print("Caesar Cipher Program")
print()

# Ask the user if they want to encrypt or decrypt the text
print("Do you want to encrypt or decrypt (e/d)?: ")
user_input = input('e/d: ').lower()

# Process encryption if the user selected 'e'
if user_input == 'e':
    print('ENCRYPTION MODE')
    print()
    # Ask for the key and the text to encrypt
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')
    # Call the encryption function and display the encrypted text
    ciphertext = encypt_decrypt(text, user_input, key)
    print(f'CIPHERTEXT: {ciphertext}')

# Process decryption if the user selected 'd'
elif user_input == 'd':
    print('DECRYPTION MODE')
    print()
    # Ask for the key and the text to decrypt
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to decrypt: ')
    # Call the decryption function and display the decrypted text
    plaintext = encypt_decrypt(text, user_input, key)
    print(f'PLAINTEXT: {plaintext}')
