# -*- coding:utf-8 -*-
import sys
import os
from PIL import Image

def blend(im1Path, im2Path, ratio=0.5):
    im1 = Image.open(im1Path)
    im2 = Image.open(im2Path)
    im2 = im2.resize(im1.size, Image.BILINEAR)
    im3 = Image.blend(im1, im2, ratio)
    return im3


if __name__ == '__main__':
    if len(sys.argv) != 5 and len(sys.argv) != 4:
        print('usage: python {} new_im_path im1_path im2_path ratio(default=0.5)'.format(sys.argv[0]))
        sys.exit(1)
    ratio = 0.5
    if len(sys.argv) == 5:
        ratio = float(sys.argv[4])
    imPath1 = sys.argv[2]
    imPath2 = sys.argv[3]
    newPath = sys.argv[1]

    im3 = blend(imPath1, imPath2, ratio)
    im3.save(newPath)
        
