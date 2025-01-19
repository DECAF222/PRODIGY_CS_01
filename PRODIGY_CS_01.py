message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))

encrypted_message = ""
for char in message:
    if char.isalpha():
        # Shift character within alphabet
        shift_base = 65 if char.isupper() else 97
        encrypted_message += chr((ord(char) - shift_base + shift_value) % 26 + shift_base)
    else:
        encrypted_message += char  # Non-alphabetic characters are added as is

print(f"Encrypted message: {encrypted_message}")

decrypted_message = ""
for char in encrypted_message:
    if char.isalpha():
        # Shift character within alphabet
        shift_base = 65 if char.isupper() else 97
        decrypted_message += chr((ord(char) - shift_base - shift_value) % 26 + shift_base)
    else:
        decrypted_message += char  # Non-alphabetic characters are added as is

print(f"Decrypted message: {decrypted_message}")
