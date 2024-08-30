def encrypt_caesar(plaintext, shift):
    encrypted_text = ""

    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26
            if char.isupper():
                start = ord('A')  # ASCII value of 'A'
            else:
                start = ord('a')  # ASCII value of 'a'

            encrypted_char = chr(start + (ord(char) - start + shift_amount) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Keep non-letters unchanged

    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

# Example usage
if __name__ == "__main__":
    plaintext = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))

    encrypted_text = encrypt_caesar(plaintext, shift)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = decrypt_caesar(encrypted_text, shift)
    print(f"Decrypted text: {decrypted_text}")
