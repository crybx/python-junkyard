# if "No module named 'cv2'"
# pip install opencv-python
import cv2
import numpy as np

# if you've never used tesseract on your pc before
# download and intall tesseract from https://github.com/UB-Mannheim/tesseract/wiki
# then:
# pip install pytesseract
import pytesseract

# If tesseract isn't in your PATH, you need this to  
# point to your tesseract install directory.
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# change path to your own test image
img = cv2.imread('ocr-test-files/notebook2.jpg')

# These lines can be skipped if you have a black and white image
#gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#gray = cv2.bitwise_not(img_bin)

# morphological operations to remove noise around the characters.
kernel = np.ones((2, 1), np.uint8)
#img = cv2.erode(gray, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=1)
out_below = pytesseract.image_to_string(img)

# lol, this kind of worked
print("OUTPUT:", out_below)

#OUTPUT: “Through primrose tufts jin thar green lower,
#The periwinkle trailed its Wreaths }
#Rind ‘tis my faith thar every Flower
#Enjoys dhe air it breathes.
#
#— WW
#♀