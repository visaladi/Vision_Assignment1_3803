import cv2
import numpy as np
import os

def block_average(block_size):
    input_path =  r"C:\Users\visal Adikari\OneDrive\Desktop\uni sem 7\vision\ass1\Assignment1\input\img1.jpg"
    output_folder = r"C:\Users\visal Adikari\OneDrive\Desktop\uni sem 7\vision\ass1\Assignment1\output"
    output_filename = f"block_avg_{block_size}x{block_size}.png"
    output_path = os.path.join(output_folder, output_filename)

    img = cv2.imread(input_path)
    if img is None:
        print("Error: Could not read the image.")
        return

    (h, w) = img.shape[:2]
    out_img = img.copy()

    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            y_end = min(y + block_size, h)
            x_end = min(x + block_size, w)

            block = img[y:y_end, x:x_end]
            if block.size == 0:
                continue

            avg_color = block.mean(axis=(0, 1)).astype(np.uint8)
            out_img[y:y_end, x:x_end] = avg_color

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cv2.imwrite(output_path, out_img)
    print(f"Block-averaged image ({block_size}x{block_size}) saved to {output_path}.")

# Run examples
block_average(3)
block_average(5)
block_average(7)
