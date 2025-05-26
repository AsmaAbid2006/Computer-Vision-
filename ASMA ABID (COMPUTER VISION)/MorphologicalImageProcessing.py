import cv2
import numpy as np
def custom_erode(image, kernel):
    h, w = image.shape
    kh, kw = kernel.shape
    new_image = np.zeros((h, w), dtype=np.uint8)
    offset_h = kh // 2
    offset_w = kw // 2
    for i in range(offset_h, h - offset_h):
        for j in range(offset_w, w - offset_w):
            region = image[i-offset_h:i+offset_h+1, j-offset_w:j+offset_w+1]
            new_image[i, j] = np.min(region * kernel)
    return new_image
def custom_dilate(image, kernel):
    h, w = image.shape
    kh, kw = kernel.shape
    new_image = np.zeros((h, w), dtype=np.uint8)
    offset_h = kh // 2
    offset_w = kw // 2
    for i in range(offset_h, h - offset_h):
        for j in range(offset_w, w - offset_w):
            region = image[i-offset_h:i+offset_h+1, j-offset_w:j+offset_w+1]
            new_image[i, j] = np.max(region * kernel)
    return new_image
def custom_open(image, kernel):
    eroded = custom_erode(image, kernel)
    opened = custom_dilate(eroded, kernel)
    return opened
def custom_close(image, kernel):
    dilated = custom_dilate(image, kernel)
    closed = custom_erode(dilated, kernel)
    return closed
def custom_gradient(image, kernel):
    dilated = custom_dilate(image, kernel)
    eroded = custom_erode(image, kernel)
    gradient = dilated - eroded
    return gradient
def main():
    image = cv2.imread('Task5/image2.jpg', 0)
    kernel = np.ones((3, 3), dtype=np.uint8)
    operation = input("Choose operation: erode, dilate, open, close, gradient: ").strip().lower()
    if operation == 'erode':
        result = custom_erode(image, kernel)
        window_title = 'Eroded Image'
    elif operation == 'dilate':
        result = custom_dilate(image, kernel)
        window_title = 'Dilated Image'
    elif operation == 'open':
        result = custom_open(image, kernel)
        window_title = 'Opened Image'
    elif operation == 'close':
        result = custom_close(image, kernel)
        window_title = 'Closed Image'
    elif operation == 'gradient':
        result = custom_gradient(image, kernel)
        window_title = 'Gradient Image'
    else:
        print("Invalid operation. Please choose from 'erode', 'dilate', 'open', 'close', or 'gradient'.")
        return
    cv2.imshow(window_title, result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    output_filename = f"{operation}_output.jpg"
    cv2.imwrite(output_filename, result)
    print(f"Result saved as {output_filename}")
if __name__ == "__main__":
    main()
