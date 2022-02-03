import easyocr
import cv2
import math
import numpy as np
import os
import sys
import ctypes

def get_line(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points

def check_black(x1, y1, x2, y2, gray):
    pts = get_line(x1, y1, x2, y2)
    for pt in pts:
        if gray[pt[1]][pt[0]][0] == 0:
            return True
    return False

# Remove all files within the Input_Image directory
# fileList = listdir('Input_image')
# for f in fileList:
#     remove('Input_image/' + f)

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

# Check the current file path
# ctypes.windll.user32.MessageBoxW(0, application_path, "Current path", 1)

# Look for all files in the Input_Image directory
fileList = os.listdir(os.path.join(application_path, 'Input_image'))

for f in fileList:
    reader = easyocr.Reader(['ch_tra','en'], gpu=True)
    result = reader.readtext(os.path.join(application_path, 'Input_image/' + f))

    img = cv2.imread(os.path.join(application_path, 'Input_image/' + f))
    res = img.copy()
    mask = np.zeros(img.shape[:2],dtype=np.uint8)

    for i in result:
        cv2.rectangle(mask, (math.floor(i[0][0][0]),math.floor(i[0][0][1])), (math.floor(i[0][2][0]),math.floor(i[0][2][1])), (255), 2)

    countours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    ret,gray = cv2.threshold(img,170,255,cv2.THRESH_BINARY)

    rightContours = []

    for c in countours:
        contourNoBlack = True
        for i, pt in enumerate(c):
            if i == 0:
                x0,y0 = pt[0]
                x1,y1 = c[-1][0]
                if check_black(x0,y0,x1,y1,gray):
                    contourNoBlack = False
                    break
            else:
                x0,y0 = pt[0]
                x1,y1 = c[i - 1][0]
                if check_black(x0,y0,x1,y1,gray):
                    contourNoBlack = False
                    break

        if contourNoBlack:
            rightContours.append(c)

    for c in rightContours:
        # cv2.drawContours(res,[c],0,(0,255,0),2)
        cv2.fillPoly(res, pts = rightContours, color=(255,255,255))

    cv2.imwrite(os.path.join(application_path, 'Output_image/' + f), res)
    # cv2.imshow("Final",res)
    # cv2.waitKey(0)


