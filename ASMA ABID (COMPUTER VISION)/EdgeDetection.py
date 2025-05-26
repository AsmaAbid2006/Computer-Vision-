from PIL import Image, ImageFilter
def detect_edges(image_path):
    try:
        image = Image.open(image_path)
        edges = image.filter(ImageFilter.FIND_EDGES)
        edges.save('edges.jpg')
        print("Edges detected and saved successfully!")
    except FileNotFoundError:
        print("Error: Image file not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", str(e))
def main():
    image_path = 'Task5/image2.jpg'  
    detect_edges(image_path)
if __name__ == "__main__":
    main()