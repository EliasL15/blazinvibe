from PIL import Image
import os

input_folder = "./"
output_folder = "./"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.startswith("image"):
        img = Image.open(input_folder + filename)
        webp_filename = os.path.splitext(filename)[0] + ".webp"
        img.save(output_folder + webp_filename, "WEBP", quality=100)
print("Conversion Complete!")
