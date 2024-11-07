# Caesar Cipher Program

## Overview

This program implements a simple Caesar Cipher encryption and decryption technique, allowing users to securely encode and decode messages using a key. The Caesar cipher is one of the earliest and simplest methods of encryption, where each letter in the plaintext is shifted by a certain number of positions in the alphabet.

## Features

- **Encryption Mode**: Users can encrypt a given message by providing a key (integer between 1 and 26). 
- **Decryption Mode**: Users can decrypt a message by using the correct key that was used during encryption.
- **Works with lowercase English letters**: The program shifts letters in the English alphabet. Non-alphabet characters such as spaces or punctuation are ignored.
  
## How It Works

- The user is asked whether they want to encrypt or decrypt a message.
- For encryption, the program shifts each letter of the input message forward by the key value.
- For decryption, the program shifts the letters backward by the key value.
- The alphabet is treated as a circular loop, so if a letter is shifted beyond 'z' or before 'a', it wraps around.
  
## Getting Started

### Requirements
- Python 3.x

### Running the Program

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Maflores1/encrytor-decryptor-poject.git
    ```

2. Navigate to the project directory:
    ```bash
    cd caesar-cipher
    ```

3. Run the Python script:
    ```bash
    python caesar_cipher.py
    ```

### Example

1. **Encryption**: 
    - Input: `e` (for encrypt), Key: `3`, Text: `hello`
    - Output: `khoor`
    
2. **Decryption**: 
    - Input: `d` (for decrypt), Key: `3`, Text: `khoor`
    - Output: `hello`
  
## See you soon!!
