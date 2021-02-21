import pytesseract
import subprocess
import os
import cv2
import json

def image_to_caption(image):
    '''
    OpenCV image -> str caption
    '''
    os.chdir('image_captions')
    if not os.path.isdir('raw_images'):
        subprocess.call('mkdir raw_images', shell=True)
    cv2.imwrite('raw_images/image.jpg', image)
    os.chdir('ImageCaptions')
    subprocess.call('python tools/eval.py --model models/trans_nsc/model-best.pth --infos_path models/trans_nsc/infos_trans_nscl-best.pkl --image_folder ../raw_images/ --num_images 1', shell=True)
    os.chdir('..')
    with open('ImageCaptions/vis/vis.json', 'r') as f:
        raw_result = json.load(f)
    subprocess.call('rm raw_images/image.jpg', shell=True)
    os.chdir('..')
    return raw_result[0]['caption']

