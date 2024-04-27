from PIL import Image
import os

def count_colors(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    colors = img.getcolors(maxcolors=999999)
    return len(colors)

def separate_images(source_folder, photos_folder, illustrations_folder):
    for filename in os.listdir(source_folder):
        try:
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".bmp") or filename.endswith(".JPG") or filename.endswith(".PNG") or filename.endswith(".BMP"):
                image_path = os.path.join(source_folder, filename)
                num_colors = count_colors(image_path)
                if num_colors > 200000:  # 閾値を設定
                    destination_folder = photos_folder
                else:
                    destination_folder = illustrations_folder
                os.rename(image_path, os.path.join(destination_folder, filename))
        except:
            print('Error: ' + filename)

if __name__ == "__main__":
    source_folder = "."
    photos_folder = ".\\photos"
    illustrations_folder = ".\\illustrations"
    
    if not os.path.exists(photos_folder):
        os.makedirs(photos_folder)
    if not os.path.exists(illustrations_folder):
        os.makedirs(illustrations_folder)
    
    separate_images(source_folder, photos_folder, illustrations_folder)
