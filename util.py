import numpy as np
import cv2
import imutils
from fast_plate_ocr import ONNXPlateRecognizer
from ultralytics import YOLO
import os

# default model, trained on data from kaggle dataset
#self trained YOLO model with high accuracy (99%)
# yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
best_detector = YOLO('best.pt')

# Using YOLO model from:
# https://github.com/mendez-luisjose/License-Plate-Detection-with-YoloV8-and-EasyOCR/blob/main/models/license_plate_detector.pt
license_plate_detector = YOLO('license_plate_detector.pt')
m = ONNXPlateRecognizer('european-plates-mobile-vit-v2-model')
output_crop_dir = "out/crop"
os.makedirs(output_crop_dir, exist_ok=True)

def four_point_transform(image, pts):
    # Order points: top-left, top-right, bottom-right, bottom-left
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # Compute width and height of new image
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # Destination points
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    # Compute perspective transform matrix and apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped


def order_points(pts):
    # Initialize a list of coordinates in order:
    # top-left, top-right, bottom-right, bottom-left
    rect = np.zeros((4, 2), dtype="float32")

    # Top-left point will have smallest sum
    # Bottom-right point will have largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # Top-right point will have smallest difference
    # Bottom-left will have largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect




def polish_plate_correction(text):
    # Convert to uppercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text.upper() if c.isalnum())

    # Define common OCR misreads (numbers that should be letters)
    number_to_letter = {
        '0': 'O',
        '1': 'I',
        '5': 'S',
        '8': 'B',
        '2': 'Z'
    }

    # Determine how many starting characters to correct
    if len(text) == 7:  # Format: LLNNNNN (2 letters + 5 alphanumeric)
        correct_length = 2
    elif len(text) == 8:  # Format: LLLNNNNN (3 letters + 5 alphanumeric)
        correct_length = 3
    else:
        return text  # Return as-is if length doesn't match expected formats

    # Correct only the first N characters
    corrected_chars = []
    for i, char in enumerate(text):
        if i < correct_length:
            # Replace numbers with letters in the first part
            corrected_chars.append(number_to_letter.get(char, char))
        else:
            # Leave the rest unchanged
            corrected_chars.append(char)

    corrected_text = ''.join(corrected_chars)
    return corrected_text

def process_image(image_path, image_name, detector = best_detector):

    crop_text = "NA"
    load_picture = cv2.imread(image_path)
    resized = imutils.resize(load_picture, width=1200)

    license_plates = detector(resized)[0]
    for license_plate in license_plates.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = license_plate
        license_plate_crop = resized [int(y1):int(y2), int(x1): int(x2), :]

        license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
        result = m.run(license_plate_crop_gray)
        #print(result)
        if result:
            crop_text = polish_plate_correction(result[0])
            print("Detected License Plate:", crop_text)
        else:
            print("License plate could not be read.")

        cv2.imwrite(os.path.join(output_crop_dir, image_name), license_plate_crop)
    return (image_name, crop_text)


def process_image_benchmark(image_path, image_name):
    return process_image(image_path, image_name, license_plate_detector)


def calculate_final_grade(accuracy_percent: float, processing_time_sec: float) -> float:
    # Check minimum requirements
    if accuracy_percent < 60 or processing_time_sec > 60:
        return 2.0
    # Normalize accuracy: 60% → 0.0, 100% → 1.0
    accuracy_norm = (accuracy_percent - 60) / 40
    # Normalize time: 60s → 0.0, 10s → 1.0
    time_norm = (60 - processing_time_sec) / 50
    # Compute weighted score
    score = 0.7 * accuracy_norm + 0.3 * time_norm
    grade = 2.0 + 3.0 * score
    # Round to the nearest 0.5
    return round(grade * 2) / 2
