import argparse
import sys
def install_pillow():
    try:
        import pip
        pip.main(['install', 'Pillow'])
    except Exception as e:
        print("An error occurred while installing Pillow:", e)
        sys.exit(1)


def get_pixel_colors(image_path):

    img = Image.open(image_path)

    width, height = img.size

    pixel_colors = []
    print("Working on it.\nPlease Wait...")
    for y in range(height):
        for x in range(width):
            color = img.getpixel((x, y))
            pixel_colors.append((x + 1, y + 1, color))
    
    return pixel_colors

def print_pixel_colors_to_file(colors, filename):
    with open(filename, 'w') as f:
        for pixel in colors:
            column, row, color = pixel
            f.write(f"[c{column}, r{row}]: rgb{color}\n")

def main():
    image_path = input("Enter the path to the image: ")
    try:
        colors = get_pixel_colors(image_path)
        image_name = image_path.split("\\")[-1].split(".")[0]
        output_filename = f"results\\{image_name}_colors.txt"
        print_pixel_colors_to_file(colors, output_filename)
        print(f"Pixel colors saved to {output_filename}")
    except Exception as e:
        print("An error occurred:", e)



try:
    from PIL import Image
except ModuleNotFoundError:
    print("Library is not installed. Installing...")
    install_pillow()    
    from PIL import Image
if __name__ == "__main__":
    main()
