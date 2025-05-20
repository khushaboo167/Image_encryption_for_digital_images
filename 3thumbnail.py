
# from PIL import Image
# import numpy as np

# # Function to create a thumbnail of an image
# def create_thumbnail(image_path, thumbnail_size=(64, 64)):
#     img = Image.open(image_path)
#     img.thumbnail(thumbnail_size)
#     return img

# # Function to encrypt the image using a thumbnail
# def encrypt_image(image_path, thumbnail_path, encrypted_image_path):
#     try:
#         # Open original image
#         pixel = Image.open(image_path).convert("RGB")
#         original_array = np.array(pixel)

#         # Create or load thumbnail
#         thumbnail = create_thumbnail(image_path)  # Corrected here
#         thumbnail_array = np.array(thumbnail.resize(pixel.size))

#         # XOR encryption
#         encrypted_array = original_array ^ thumbnail_array

#         # Save encrypted image
#         encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
#         encrypted_img.save(pixel.jpg)
#         print("Image encrypted successfully.")
#     except Exception as e:
#         print(f"Error: {e}")

# # Function to decrypt the image
# def decrypt_image(encrypted_image_path, thumbnail_path, decrypted_image_path):
#     try:
#         # Open encrypted image
#         encrypted_img = Image.open(encrypted_image_path).convert("RGB")
#         encrypted_array = np.array(pixel.jpg)

#         # Load thumbnail and resize to match original image
#         thumbnail = create_thumbnail(pixel.jpg)  # Corrected here
#         thumbnail_array = np.array(thumbnail.resize(pixel.size))

#         # XOR decryption
#         decrypted_array = encrypted_array ^ thumbnail_array

#         # Save decrypted image
#         decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
#         decrypted_img.save(pixel.jpg)
#         print("Image decrypted successfully.")
#     except Exception as e:
#         print(f"Error: {e}")

# # Example usage
# image_path = "pixel.jpg"
# thumbnail_path = "pixel.jpg"  # Corrected here
# encrypted_image_path = "pixel.jpg"
# decrypted_image_path = "pixel.jpg"

# encrypt_image(image_path, thumbnail_path, encrypted_image_path)
# decrypt_image(encrypted_image_path, thumbnail_path, decrypted_image_path)








# correct code

from PIL import Image
import numpy as np

# Function to create a thumbnail of an image
def create_thumbnail(image_path, thumbnail_size=(64, 64)):
    img = Image.open(image_path)
    img.thumbnail(thumbnail_size)
    return img

# Function to encrypt the image using a thumbnail
def encrypt_image(image_path, thumbnail_path, encrypted_image_path):
    try:
        # Open original image
        original_img = Image.open(image_path).convert("RGB")
        original_array = np.array(original_img)

        # Create or load thumbnail
        thumbnail = create_thumbnail(image_path)
        thumbnail_array = np.array(thumbnail.resize(original_img.size))

        # XOR encryption
        encrypted_array = original_array ^ thumbnail_array

        # Save encrypted image
        encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
        encrypted_img.save(encrypted_image_path)
        print("Image encrypted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Function to decrypt the image
def decrypt_image(encrypted_image_path, thumbnail_path, decrypted_image_path):
    try:
        # Open encrypted image
        encrypted_img = Image.open(encrypted_image_path).convert("RGB")
        encrypted_array = np.array(encrypted_img)

        # Load thumbnail and resize to match original image
        thumbnail = create_thumbnail(image_path)
        thumbnail_array = np.array(thumbnail.resize(encrypted_img.size))

        # XOR decryption
        decrypted_array = encrypted_array ^ thumbnail_array

        # Save decrypted image
        decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
        decrypted_img.save(decrypted_image_path)
        print("Image decrypted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
image_path = "C:/Users/asus/Desktop/python/project/pixels.jpg"
thumbnail_path = "C:/Users/asus/Desktop/python/project/thumbnail_pexels.jpg"

encrypted_image_path = "C:/Users/asus/Desktop/python/project/encrypted_pixels.jpg"

decrypted_image_path = "C:/Users/asus/Desktop/python/project/decrypted_pixels.jpg"


encrypt_image(image_path, thumbnail_path, encrypted_image_path)
decrypt_image(encrypted_image_path, thumbnail_path, decrypted_image_path)
