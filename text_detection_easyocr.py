import easyocr
import cv2
import math
import numpy as np

imgPath = 'sample4.jpg'
reader = easyocr.Reader(['ch_tra','en'],gpu=True)
result = reader.readtext(imgPath)

img = cv2.imread(imgPath)
res = img.copy()
mask = np.zeros(img.shape[:2],dtype=np.uint8)

for i in result:
    cv2.rectangle(mask, (math.floor(i[0][0][0]),math.floor(i[0][0][1])), (math.floor(i[0][2][0]),math.floor(i[0][2][1])), (255), 2)

countours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for c in countours:
    cv2.drawContours(res,[c],0,(0,255,0),2)

cv2.imshow("Contour",res)
cv2.waitKey(0)