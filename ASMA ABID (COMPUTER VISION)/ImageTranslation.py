from PIL import Image
def translate_image(image_path, x_offset, y_offset):
    try:
        image = Image.open(image_path)
        width, height = image.size
        translated_image = Image.new(image.mode, (width + abs(x_offset), height + abs(y_offset)))
        translated_image.paste(image, (x_offset, y_offset))
        translated_image.save('translated_image.jpg')
        print("Image translated and saved successfully!")
    except FileNotFoundError:
        print("Error: Image file not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", str(e))
def main():
    image_path = 'Task5/image2.jpg'  
    x_offset = 50  
    y_offset = 100
    translate_image(image_path, x_offset, y_offset)
if __name__ == "__main__":
    main()