import os
from PIL import Image

# image_names = <main_tag>/<tag>/<serial_num>.png
def load_images_with_tag_from_directory(directory, transform, device):
    image_list = []
    image_names = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".png"):
                file = os.path.join(root, file)
                img = Image.open(file).convert("RGB")
                img = transform(img).unsqueeze(0)  # Add batch dimension
                image_list.append(img.to(device))
                image_names.append(file)
    return image_list, image_names
