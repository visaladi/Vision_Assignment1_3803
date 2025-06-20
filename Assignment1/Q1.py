#q1
#author:- visal adikari

import cv2
import numpy as np
import os

def reduce_intensity_levels(levels):
    input_path = "Assignment1/input/img1.jpg"
    output_folder = "Assignment1/output"
    output_path = os.path.join(output_folder, "reduced_levels.png")

    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Could not read the image.")
        return

    factor = 256 // levels
    reduced = (img // factor) * factor

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cv2.imwrite(output_path, reduced)
    print(f"Image saved to {output_path} with {levels} intensity levels.")

# Run with 2 intensity levels
reduce_intensity_levels(2)
