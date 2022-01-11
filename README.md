## Recognizing vertical traditional chinese text
My initial target is to clean comics with vertical traditional chinese text. So I needed an OCR that can accurately recognize that. Unfortunately, most of the well-known OCR tools were not developed for that. I tested quite a few tools to find out that easy OCR should be the one most suitable for my use case. I kept all the testing script in the OCR_test directory

### East text detection
Seems to be one of the popular OCR tool. It has the advantage that only opencv need to be installed. But it doesn't recognize chinese text well.

Reference: https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/

### Tesseract
One of the most famous open source OCR tool. Need to install tesseract before using it. Also need to find the respective language tesseract file to use it. Tried a lot of different configuration. PSM 12 and OEM 1 seems to be the most optimal for my use case. But still not satisfactory

### Easy OCR
Come across this tool in some chinese blog. It recognized vertical chinese text almost perfectly. Used this tool in my final script.


# To be continued