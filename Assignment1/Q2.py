import cv2
import os

def average_filter(kernel_size):
    input_path = r"C:\Users\visal Adikari\OneDrive\Desktop\uni sem 7\vision\ass1\Assignment1\input\img1.jpg"
    output_folder = r"C:\Users\visal Adikari\OneDrive\Desktop\uni sem 7\vision\ass1\Assignment1\output"
    output_filename = f"avg_{kernel_size}x{kernel_size}.png"
    output_path = os.path.join(output_folder, output_filename)

    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Could not read the image.")
        return

    blurred = cv2.blur(img, (kernel_size, kernel_size))

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cv2.imwrite(output_path, blurred)
    print(f"Image saved to {output_path} with {kernel_size}x{kernel_size} average filter.")

# Run examples
average_filter(3)
average_filter(10)
average_filter(20)
