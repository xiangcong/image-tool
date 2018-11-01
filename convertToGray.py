import PIL
import sys
import os
from PIL import Image

def convert(path):
    im = Image.open(path).convert('L')
    dotPos = path.rfind('.')
    newPath = path[0:dotPos] + 'Gray' + '.jpg'
    im.save(newPath)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python {} imagePath'.format(sys.argv[0]))
    else:
        convert(sys.argv[1])


