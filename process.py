from text_summaries import summarize, segment
from image_captions import captions
import pytesseract
import cv2
import numpy as np

def process(image_path):
    ### 1: IMAGE SEGMENTATION ###

    '''
    The first section of this code extracts the coordinates of all of the image
    regions from within a given image (defined as rectangular regions within a document)
    '''

    img = cv2.imread(image_path)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))

    dilated = cv2.dilate(grey, kernel)
    _, thresholded = cv2.threshold(dilated, 254, 255, cv2.THRESH_TOZERO)
    _, thresholded = cv2.threshold(thresholded, 0, 255, cv2.THRESH_BINARY_INV)

    morph = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)
    morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

    contours, hierarchy = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    squares = []

    images = []

    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) > 1000:
            box = cv2.approxPolyDP(contours[i], 50, True)
            squares.append(box)
            contour_temp = []
            contour_temp.append(box)
            mask = np.zeros_like(grey)
            cv2.drawContours(mask, contour_temp, 0, (255, 255, 255), -1)
            out = np.zeros_like(img)
            out[mask == 255] = img[mask == 255]

            (y, x) = np.where(mask == 255)
            (topy, topx) = (np.min(y), np.min(x))
            (bottomy, bottomx) = (np.max(y), np.max(x))
            out = out[topy:bottomy+1, topx:bottomx+1]
            images.append(out)

    ### 2: CAPTIONING ###

    image_captions = []

    for image in images:
        try:
            image_captions.append(captions.image_to_caption(image)) # for each image, generate captions
        except:
            print('Warning! Caption generation failed!')

    print(image_captions)

    ### 3: TEXT RECOGNITION ###

    _, binary_img = cv2.threshold(grey, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # threshold image for tesseract performance gains
    raw_text = pytesseract.image_to_string(binary_img) # extract text from image

    ### 4: SUMMARIZATION ###
    segmented_paragraphs = segment(raw_text)
    for i in range(len(segmented_paragraphs)):
        segmented_paragraphs[i] = segmented_paragraphs[i].strip() # eliminate empty chars/stops, etc

    segmented_paragraphs = list(filter(None, segmented_paragraphs)) # filter out empty paragraphs
    summaries = summarize(segmented_paragraphs)

    ### 5: COMBINE RESULTS ###
    overall_desc = {'bullets': summaries, 'image_descs': image_captions}

    return overall_desc

