import cv2
import numpy as np
from skimage import io
import pytesseract
import shutil
import os
import random
import sys
from utilities import Image

# IMAGES
cards = Image('img/cards.jpg')

cards_rgb = cards.conversion('rgb')
cards_gray = cards.conversion('gray')
cards_blurred = cards.blur()
cards_gray_blur = cards.gray_blur()

if __name__ == '__main__':
    if sys.argv[1] == '1':
        img = cards.img_
    elif sys.argv[1] == '2':
        img = cards_rgb
    elif sys.argv[1] == '3':
        img = cards_gray
    elif sys.argv[1] == '4':
        img = cards_gray_blur


    # # SHAPE
    # print('(largura, altura, canais)', img.shape)
    # # PIXEL INDIVIDUAL
    # print("Pixel individual (BGR): \n", img[200][300]) #input [y][x] outpup [B][G][R]


    
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
