## Recognizing vertical traditional chinese text
My initial target is to clean comics with vertical traditional chinese text. So I needed an OCR that can accurately recognize that. Unfortunately, most of the well-known OCR tools were not developed for that. I tested quite a few tools to find out that easy OCR should be the one most suitable for my use case. I kept all the testing script in the OCR_test directory

Input image:
![Input Image](https://github.com/matthewmakhl/Empty-Comic-Dialog-box/blob/main/README_images/Input_image.PNG)


## OCR

### East text detection
Seems to be one of the popular OCR tool. It has the advantage that only opencv need to be installed. But it doesn't recognize chinese text well.

Reference: https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/

![East text detection Image](https://github.com/matthewmakhl/Empty-Comic-Dialog-box/blob/main/README_images/East_text_detector.PNG)

### Tesseract
One of the most famous open source OCR tool. Need to install tesseract before using it. Also need to find the respective language tesseract file to use it. Tried a lot of different configuration. PSM 12 and OEM 1 seems to be the most optimal for my use case. But still not satisfactory

![Tesseract detection Image](https://github.com/matthewmakhl/Empty-Comic-Dialog-box/blob/main/README_images/Tesseract.PNG)

### Easy OCR
Come across this tool in some chinese blog. It recognized vertical chinese text almost perfectly. Used this tool in my final script.

![Easy OCR detection Image](https://github.com/matthewmakhl/Empty-Comic-Dialog-box/blob/main/README_images/Easy_ocr.PNG)


## Cleaning

I just coded the script to do some simple cleaning at this point. It first copied another images and turned the copied images into black and white scale. If the border of the green boxes detected in the previous step doesn't touch any black line at all, the script will turn everything in the boxes as white.

Result image:
![Output Image](https://github.com/matthewmakhl/Empty-Comic-Dialog-box/blob/main/README_images/Output_image.PNG)

The cleaning method can certainly be improved. But I cannot think of an easy method to do it right now. I will think of it if there is really demand for this tool. Currently it is only for my own experiment.

## Pre-release
I used the Pyinstaller library to create a exe file for easier installation. If you follow the guide here (https://github.com/matthewmakhl/Empty-Comic-Dialog-box/releases), you can use the cleaning tool without installing Python.

Note for my future self, the Pyinstaller won't grab the Easy OCR module itself, so you would need to instruct it in the command to grab Easy OCR as well.
