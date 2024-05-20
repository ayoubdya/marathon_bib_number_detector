import cv2
import numpy as np
import imutils
from PIL import Image
from deskew import determine_skew
import pickle


def add_padding(img, box, padding=10):
    x1, y1, x2, y2 = box
    h, w = img.shape[:2]
    x1 = max(0, x1 - padding)
    y1 = max(0, y1 - padding)
    x2 = min(w, x2 + padding)
    y2 = min(h, y2 + padding)
    return x1, y1, x2, y2


def deskew(image, angle):
    '''
    This function helps adjusts the image according to the determined skew angle as apart of the image pre-processing for optimal
    OCR results. 
    '''
    non_zero_pixels = cv2.findNonZero(cv2.bitwise_not(image))
    center, _, _ = cv2.minAreaRect(non_zero_pixels)  # _, _ = wh, theta

    root_mat = cv2.getRotationMatrix2D(center, angle, 1)
    rows, cols = image.shape
    rotated = cv2.warpAffine(
        image, root_mat, (cols, rows), flags=cv2.INTER_CUBIC)

    return rotated


def crop_dark_regions(image):
    '''
    This function removes the border of the image. A dark border can skew characterizations. 
    '''
    mask = np.zeros(image.shape, dtype=np.uint8)

    cnts = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    cv2.fillPoly(mask, cnts, [255, 255, 255])
    mask = 255 - mask
    result = cv2.bitwise_or(image, mask)

    return result


def preprocess_cropped(cropped):
    img = imutils.resize(cropped, width=300)  # type = np.array
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    angle = determine_skew(img)
    img = deskew(img, angle)
    img = crop_dark_regions(img)
    img = cv2.bilateralFilter(img, 11, 17, 17)
    img = crop_dark_regions(img)
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # img = img.filter(ImageFilter.GaussianBlur(radius=1))
    return img
