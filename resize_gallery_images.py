from PIL import Image
import os

def resize_image(image_path, width, height):
    with Image.open(image_path) as img:
        # Calculate center crop coordinates
        left = (img.width - width) // 2
        top = (img.height - height) // 2
        right = left + width
        bottom = top + height
        
        # Perform center crop
        cropped = img.crop((left, top, right, bottom))
        
        # Save with optimized settings
        cropped.save(image_path, 'WEBP', quality=100, optimize=True)

def process_gallery():
    gallery_path = os.path.join(os.path.dirname(__file__), './')
    target_width = 300
    target_height = 200
    
    # Process each image in the gallery
    for filename in os.listdir(gallery_path):
        if filename.lower().startswith('image10.webp'):
            image_path = os.path.join(gallery_path, filename)
            print(f'Processing {filename}...')
            try:
                resize_image(image_path, target_width, target_height)
                print(f'Successfully resized {filename}')
            except Exception as e:
                print(f'Error processing {filename}: {str(e)}')

if __name__ == '__main__':
    process_gallery()