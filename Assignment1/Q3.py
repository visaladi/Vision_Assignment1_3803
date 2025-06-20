import cv2
import os

def rotate_image(angle):
    input_path = r"C:\Users\visal Adikari\OneDrive\Desktop\uni sem 7\vision\ass1\Assignment1\input\img1.jpg"
    output_folder =  r"C:\Users\visal Adikari\OneDrive\Desktop\uni sem 7\vision\ass1\Assignment1\output"
    output_filename = f"rotated_{angle}.png"
    output_path = os.path.join(output_folder, output_filename)

    img = cv2.imread(input_path)
    if img is None:
        print("Error: Could not read the image.")
        return

    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, matrix, (w, h))

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cv2.imwrite(output_path, rotated)
    print(f"Image rotated by {angle}° and saved to {output_path}.")

# Run examples
rotate_image(45)
rotate_image(90)
