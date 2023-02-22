import os
from PIL import Image

folder_path = input("Please enter the file or folder path: ")
new_format = input("Please enter the desired format (e.g. 'JPEG', 'PNG', etc.): ").upper()

if os.path.isfile(folder_path):
    image_files = [folder_path]
else:
    image_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif')):
                image_files.append(os.path.join(root, file))

    if not image_files:
        print("No image files found in the folder.")
        exit()

    print(f"Found {len(image_files)} image files.")
    all_images = input("Would you like to convert all Image files within this folder? (Yes/No): ")

    if all_images.lower() == "no":
        print("Select images you want to convert (Separate filenames by commas):")
        for index, file in enumerate(image_files):
            print(f"{index + 1}. {file}")
        selected_files = input()
        selected_files = [int(x.strip()) for x in selected_files.split(",")]
        image_files = [image_files[i - 1] for i in selected_files]

for file_path in image_files:
    with Image.open(file_path) as img:
        new_filename = os.path.splitext(file_path)[0] + "." + new_format.lower()
        img = img.convert('RGB')
        img.save(new_filename, format=new_format)

print("Conversion complete!")
