from PIL import Image

def encrypt_image(image_path, output_path, key):
    """Encrypts an image by manipulating its pixel values using a key."""
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    # Encrypt each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Encrypt by adding the key (mod 256 to keep within valid range)
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)

    image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    """Decrypts an image by reversing the pixel manipulation."""
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    # Decrypt each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Decrypt by subtracting the key (mod 256 to keep within valid range)
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Example usage with image paths
key = 50  # This is the key used for encryption and decryption

# Paths to input and output images
input_image_path = "C:\input image\inputimg.png"  # Replace with your image file path
encrypted_image_path = "C:\encrypt img\encryptimg.png"  # Path to save the encrypted image
decrypted_image_path = "C:\decrypt img\decryptimg.png"  # Path to save the decrypted image

# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path, key)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, key)
