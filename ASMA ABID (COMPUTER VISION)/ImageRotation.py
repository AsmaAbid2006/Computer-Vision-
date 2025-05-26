from PIL import Image
def rotate_image(image_path, angle):
    try:
        image = Image.open(image_path)
        rotated_image = image.rotate(angle)
        rotated_image.save('rotated_image.jpg')
        print("Image rotated and saved successfully!")
    except FileNotFoundError:
        print("Error: Image file not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", str(e))
def main():
    image_path = 'Task5/image2.jpg' 
    angle = 45  
    rotate_image(image_path, angle)
if __name__ == "__main__":
    main()