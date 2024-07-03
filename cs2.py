from PIL import Image
import random

def load_image(image_path):
    return Image.open(image_path)

def save_image(image, output_path):
    image.save(output_path)

def swap_pixels(image):
    pixels = image.load()
    width, height = image.size
    
    for _ in range((width * height) // 2):
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        
        # Swap pixels
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]
    
    return image

def apply_math_operation(image, operation):
    pixels = image.load()
    width, height = image.size
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            r = (r + operation) % 256
            g = (g + operation) % 256
            b = (b + operation) % 256
            pixels[x, y] = (r, g, b)
    
    return image

def encrypt_image(image_path, output_path, operation=50):
    image = load_image(image_path)
    
    # Apply pixel swapping
    image = swap_pixels(image)
    
    # Apply mathematical operation
    image = apply_math_operation(image, operation)
    
    # Save the encrypted image
    save_image(image, output_path)

def apply_inverse_math_operation(image, operation):
    pixels = image.load()
    width, height = image.size
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Apply the inverse of the mathematical operation
            r = (r - operation) % 256
            g = (g - operation) % 256
            b = (b - operation) % 256
            pixels[x, y] = (r, g, b)
    
    return image

def decrypt_image(image_path, output_path, operation=50):
    image = load_image(image_path)
    
    # Reverse the mathematical operation
    image = apply_inverse_math_operation(image, operation)
    
    # Save the decrypted image
    save_image(image, output_path)

# Example usage
decrypt_image(r"C:\Users\ASUS\Desktop\python\smile.jpg", 'decrypted_image.jpg')
