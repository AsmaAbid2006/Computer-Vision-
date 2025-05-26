from PIL import Image
def shear_image(image_path, shear_factor):
    try:
        image = Image.open(image_path)
        width, height = image.size
        shear_x = int(shear_factor * width)
        shear_y = int(shear_factor * height)
        matrix = (1, shear_factor, 0, 1, shear_x, shear_y)
        sheared_image = image.transform((width, height), Image.AFFINE, matrix)
        sheared_image.save('sheared_image.jpg')
        print("Image sheared and saved successfully!")
    except FileNotFoundError:
        print("Error: Image file not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", str(e))
def main():
    image_path = 'Task5/image2.jpg'  
    shear_factor = 0.01
    shear_image(image_path, shear_factor)
if __name__ == "__main__":
    main()