# Vigenère Cipher Implementation in Python
This repository contains a Python implementation of the Vigenère Cipher, a method of encrypting and decrypting text using a series of different Caesar ciphers based on the letters of a keyword.

## Features
- **Encryption**: Encrypt a plain text using a keyword.
- **Decryption**: Decrypt a cipher text using the same keyword used for encryption.

## How It Works
The Vigenère Cipher works by shifting each letter in the plaintext by the amount specified by the corresponding letter in the keyword. If the keyword is shorter than the plaintext, it repeats itself as necessary.

### Example
For example, if you want to encrypt the text `HELLO` with the key `KEY`, the process would look like this:

1. Align the key with the text:
Text: H E L L O Key: K E Y K E

2. Encrypt each letter:
- H shifted by K results in R
- E shifted by E results in I
- L shifted by Y results in J
- L shifted by K results in V
- O shifted by E results in S

3. The resulting ciphertext is `RIJVS`.

## Code Explanation
The main functions are:

- **`encryption(plainText, key)`**: Encrypts the given `plainText` using the provided `key`.
- **`decryption(text, key)`**: Decrypts the given `text` using the provided `key`.
- **`vigenere(text, key, mode)`**: A wrapper function that calls either `encryption` or `decryption` based on the mode selected.

### Input Parameters
- `text`: The text to be encrypted or decrypted.
- `key`: The keyword used for encryption/decryption.
- `mode`: Specify either `"encryption"` or `"decryption"`.

### Output
The program will output the encrypted or decrypted text based on the selected mode.
