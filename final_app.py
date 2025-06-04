import os
import csv
import time
import random
import xml.etree.ElementTree as ET
from collections import defaultdict

import cv2
import imutils

from util import calculate_final_grade, process_image, process_image_benchmark

def main ():
    csv_file_path = "out/result.csv"
    src_dir = "src/photos"
    xml_path = "src/annotations.xml"

    results_list = []
    all_images = [f for f in os.listdir(src_dir) if f.endswith('.jpg')]
    selected_images = random.sample(all_images, min(100, len(all_images)))

    start_time = time.time()

    for img_name in selected_images:
        img_path = os.path.join(src_dir, img_name)

        result = process_image(img_path, img_name)
        #another YOLO model with lower accuracy~95%
        #result = process_image_benchmark(img_path, img_name)
        results_list.append(result)

    end_time = time.time()
    total_time = end_time - start_time


    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Image Name', 'Crop Text'])

        # Write data rows
        csv_writer.writerows(results_list)

    print(f"\nResults saved to {csv_file_path}\n")

    correct_count_crop = 0
    total_count = len(results_list)

    # Parse the XML file
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Create a dictionary to store plate numbers by image name
    plate_numbers = defaultdict(str)

    # Extract plate numbers from XML
    for image in root.findall('image'):
        image_name = image.get('name')
        for box in image.findall('box'):
            if box.get('label') == 'plate':
                plate_number = box.find("attribute[@name='plate number']").text
                plate_numbers[image_name] = plate_number

    for result in results_list:
        image_name, crop_text = result
        xml_plate = plate_numbers.get(image_name, "NOT_FOUND_IN_XML")

        if crop_text == xml_plate:
            correct_count_crop +=1
        else:
            print(f"{image_name}:Incorrect crop: {crop_text}, expected {xml_plate}")

    crop_accuracy = int ((correct_count_crop/total_count)*100)

    print(f"\nTotal processing time: {total_time:.4f} seconds")
    print(f"Crop accuracy: {crop_accuracy} %")
    print(f"Final grade: {calculate_final_grade(crop_accuracy, total_time)}")


main()
















