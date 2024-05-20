from ultralytics import YOLO
import cv2
from tools import add_padding
import pytesseract
import re
import numpy as np
import pickle


class Detector():
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.current_image = np.array([])

    def parse_boxes(self, result):
        img = self.current_image
        boxes = result[0].boxes.xyxy.tolist()
        boxes = [list(map(int, box)) for box in boxes]
        boxes = list(map(lambda box: add_padding(img, box), boxes))
        return boxes

    def ocr_numbers(self, boxes):
        img = self.current_image
        numbers = []
        for box in boxes:
            x1, y1, x2, y2 = box
            cropped = img[y1:y2, x1:x2]
            number = pytesseract.image_to_string(
                cropped, config='--psm 8 -c tessedit_char_whitelist=0123456789')
            number = re.sub(r'\D', '', number)
            numbers.append(number)
        return numbers

    def detect(self, image_path):
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.current_image = img
        result = self.model.predict(self.current_image)
        boxes = self.parse_boxes(result)
        numbers = self.ocr_numbers(boxes)
        return numbers

    def detect_images(self, image_paths):
        result_dict = {}  # {number: [image_path]}
        for image_path in image_paths:
            numbers = self.detect(image_path)
            for number in numbers:
                if result_dict.get(number):
                    result_dict[number].append(image_path)
                else:
                    result_dict[number] = [image_path]
        return result_dict

    def dump_results(self, result_dict):
        with open("data/data.pkl", "wb") as file:
            pickle.dump(result_dict, file)

    def update_results(self, result_dict):
        with open("data/data.pkl", "rb") as file:
            data = pickle.load(file)
            for number, image_paths in result_dict.items():
                if data.get(number):
                    data[number].extend(image_paths)
                else:
                    data[number] = image_paths
        with open("data/data.pkl", "wb") as file:
            pickle.dump(data, file)
        return data
