# Caesar Cipher Encryption and Decryption

This is a simple Python program that implements the Caesar Cipher encryption and decryption algorithm. The Caesar Cipher is a basic encryption technique where each letter in the plaintext is shifted by a predefined number of positions in the alphabet.

## Features

- **Encrypts and Decrypts**: Shifts alphabetic characters by a specified value.
- **Supports Uppercase and Lowercase Letters**: Both uppercase and lowercase letters are shifted correctly.
- **Non-Alphabetic Characters**: Spaces, punctuation, and other non-alphabetic characters remain unchanged during encryption and decryption.

## How It Works

The Caesar Cipher works by shifting each letter of the alphabet by a predefined number. For example:
- A shift of 3 turns:
  - 'A' to 'D'
  - 'B' to 'E'
  - 'Z' to 'C'

The same shift value is used for both encryption and decryption. To decrypt a message, the shift is reversed.