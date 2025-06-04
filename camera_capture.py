import cv2
import numpy as np
import time
import os
from util import process_image_benchmark

#from pynput import keyboard
output_capture_dir = "out/capture"
os.makedirs(output_capture_dir, exist_ok=True)

szlaban = cv2.imread("src/szlaban.png")


allowed_plates = []

with open("src/allowed_plates.txt", "r") as f:
    allowed_plates = [line.strip() for line in f if line.strip()]

print(allowed_plates)

def take_photo():
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    for _ in range(30):  # Usually 20–30 frames (~1 sec)
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (camera disconnected?). Exiting...")
            break

        # Optional: Add a short delay between reads
        time.sleep(0.033)  # ~30 fps (1/30 sec per frame)
    ret, frame = cap.read()
    time.sleep(0.1)
    cap.release()

    if ret:
        # Increase brightness by converting to HSV and increasing V channel

        filename = f"photo_{int(time.time())}.jpg"
        print(f"{filename}")
        filepath=os.path.join(output_capture_dir, filename)

        cv2.imwrite(filepath, frame)
        #Comment for processing captured picture
        result = process_image_benchmark(filepath, filename)
        #mocked with picture already taken to ilustrate opening parking gate
        file_path = "out/capture/photo_1748778672.jpg"
        file_name = "photo_1748778672.jpg"
        result = process_image_benchmark(file_path, file_name)
        if result[1] in allowed_plates:
            #Znana rejestracja, otwieramy szlaban!
            cv2.imshow("Szlaban otwarty",szlaban)
            cv2.waitKey(2000)
            cv2.destroyWindow("Szlaban otwarty")
    else:
        print("Failed to capture image")

def create_main_picture():
    # Create a black image (height=200, width=600)
    image = np.zeros((200, 600, 3), dtype=np.uint8)

    # Define the text
    text = 'Press "p" to take a photo. Press "q" to quit.'

    # Set text properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7
    color = (255, 255, 255)  # White
    thickness = 2

    # Get the size of the text box
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)

    # Calculate position to center the text
    x = (image.shape[1] - text_width) // 2
    y = (image.shape[0] + text_height) // 2

    # Put the text on the image
    cv2.putText(image, text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)

    return image


while True:

    cv2.imshow("Instructions", create_main_picture())
    key = cv2.waitKey(1) & 0xFF

    if key == 255:
        continue  # No key pressed, ignore

    if key == ord('p'):
        take_photo()
    elif key == ord('q'):
        print("Quitting...")
        break

    else:
        print(f"Ignored key: {key}")  # For debugging (optional)

