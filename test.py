from PIL import Image
import os

input_folder = "./assets/"
output_folder = "./assets/webp/"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open(input_folder + filename)
        webp_filename = os.path.splitext(filename)[0] + ".webp"
        img.save(output_folder + webp_filename, "WEBP", quality=80)
print("Conversion Complete!")
