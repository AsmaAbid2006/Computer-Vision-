from PIL import Image
def load_image(filename):
    return Image.open(filename)
def resize_image(image, new_width, new_height):
    return image.resize((new_width, new_height))
def save_image(image, filename):
    image.save(filename)
def resize_image_file(input_filename, output_filename, new_width, new_height):
    image = load_image(input_filename)
    resized_image = resize_image(image, new_width, new_height)
    save_image(resized_image, output_filename)
def main():
    input_filename = 'Task5/image2.jpg'
    output_filename = 'Task3/Resized-Image.jpg'
    new_width = 500
    new_height = 400
    resize_image_file(input_filename, output_filename, new_width, new_height)
    print(f"Image resized and saved to {output_filename}")
if __name__ == "__main__":
    main()