from PIL import Image
import os

def resize_image(image_path, width, height):
    with Image.open(image_path) as img:
        # Calculate aspect ratio
        aspect_ratio = img.width / img.height
        new_width = width
        new_height = height

        # Resize image maintaining aspect ratio and crop if necessary
        if aspect_ratio > (width / height):
            new_width = int(height * aspect_ratio)
        else:
            new_height = int(width / aspect_ratio)

        # Resize with high-quality resampling
        resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Center crop to target size
        left = (resized.width - width) // 2
        top = (resized.height - height) // 2
        right = left + width
        bottom = top + height
        cropped = resized.crop((left, top, right, bottom))

        # Save with optimized settings
        cropped.save(image_path, 'WEBP', quality=85, optimize=True)

def process_gallery():
    gallery_path = os.path.join(os.path.dirname(__file__), 'assets')
    target_width = 300
    target_height = 200
    
    # Process each image in the gallery
    for filename in os.listdir(gallery_path):
        if filename.lower().startswith('image'):
            image_path = os.path.join(gallery_path, filename)
            print(f'Processing {filename}...')
            try:
                resize_image(image_path, target_width, target_height)
                print(f'Successfully resized {filename}')
            except Exception as e:
                print(f'Error processing {filename}: {str(e)}')

if __name__ == '__main__':
    process_gallery()