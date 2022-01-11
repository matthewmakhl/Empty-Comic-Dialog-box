# import cv2
# import pytesseract

# img = cv2.imread('sample1.jpg')
# lang = "chi_tra_vert"
# psm = 13

# h, w, c = img.shape
# options = "-l {} --psm {}".format(lang, psm)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Matthew\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
# boxes = pytesseract.image_to_boxes(img, config=options) 
# for b in boxes.splitlines():
#     b = b.split(' ')
#     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)


import cv2
import pytesseract
from pytesseract import Output
import math

img = cv2.imread('Sample_image/sample1.jpg')
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# (thresh, img) = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.waitKey(0)

lang = "chi_tra_vert"
psm = 12
oem = 1

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Matthew\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
options = "-l {} --psm {}".format(lang, psm)
# options = "-l {}".format(lang)
d = pytesseract.image_to_data(img, output_type=Output.DICT, config=options)
print(d.keys())
print(len(d['conf']))

n_boxes = len(d['text'])
for i in range(n_boxes):
	print("Text: " + d['text'][i] + ", Conf: " + d['conf'][i])
	if int(math.floor(float(d['conf'][i]))) > 60:
		(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
		img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)