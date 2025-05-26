from PIL import Image, ImageFilter
def blur_image(image_path, blur_radius):
    try:
        image = Image.open(image_path)
        blurred_image = image.filter(ImageFilter.GaussianBlur(radius=blur_radius))
        blurred_image.save('blurred_image.jpg')
        print("Image blurred and saved successfully!")
    except FileNotFoundError:
        print("Error: Image file not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", str(e))
def main():
    image_path = 'Task5/image2.jpg' 
    blur_radius = 5  
    blur_image(image_path, blur_radius)
if __name__ == "__main__":
    main()
