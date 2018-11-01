# -*- coding:utf-8 -*-
'''
resize images to the same height, 
and then form a new image
NOTE:
    Image is width*height
    Array is height*width
'''
import sys
import os
import numpy as np
from PIL import Image
import scipy.misc as misc

def stackIms(heightNorm, newPath, images):
    '''
    resize all the imags to the same height:heightNorm
    and then save as newPath

    '''
    finalWidth = getFinalWidth(images, heightNorm)
    finalImageArray = np.zeros((heightNorm, finalWidth, 3),dtype=np.int8)
    copyToFinal(finalImageArray, images)
    finalImage = Image.fromarray(finalImageArray, 'RGB')
    finalImage.save(newPath)

def getFinalWidth(images, heightNorm):
    finalWidth = 0
    for imagePath in images:
        image = Image.open(imagePath)
        size = image.size
        width = size[0]
        height = size[1]
        finalWidth += int(width * heightNorm / height)
    return int(finalWidth)

def copyToFinal(finalImageArray, images):
    widthBias = 0
    heightNorm = finalImageArray.shape[0]
    for imagePath in images:
        image = Image.open(imagePath)
        image = image.convert('RGB')
        size = image.size
        width = size[0]
        height = size[1]
        widthNorm = int(heightNorm * width / height)
        image = image.resize((widthNorm, heightNorm))
        imageArray = np.asarray(image)
        finalImageArray[:, widthBias:widthBias+widthNorm, :] = imageArray
        widthBias += widthNorm




if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('usage: python xx.py normalized_height newPath imagePath1 imagePath2 ...')
    else:
        heightNorm = int(sys.argv[1])
        newPath = sys.argv[2]
        imagesPath = sys.argv[3:]
        stackIms(heightNorm, newPath, imagesPath)
