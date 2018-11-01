import stackIms
import shutil
import sys
import os

HEIGHT = 1000

def stackImsInFolder(folders, newFolder):
    if os.path.exists(newFolder):
        shutil.rmtree(newFolder)
    os.mkdir(newFolder)
    imageNames = os.listdir(folders[0])
    for imageName in imageNames:
        if imageName.endswith('.png') or imageName.endswith('.jpg'):
            print('processing {}...'.format(imageName))
            imagePaths = []
            for folder in folders:
                imagePath = os.path.join(folder, imageName)
                # if folder.endswith('test_masks'):
                #     imagePath = imagePath[:-4] + '_seg' + '.png'
                imagePaths.append(imagePath)
            imagePathNew = os.path.join(newFolder, imageName)
            try:
                stackIms.stackIms(HEIGHT, imagePathNew, imagePaths)
            except:
                print('error!')
                continue


if __name__ == '__main__':
    if len(sys.argv) > 3:
        folderNew = sys.argv[1]
        folders = sys.argv[2:]
        stackImsInFolder(folders, folderNew)
    else:
        print('usage: python {} folderNew folder1, folder2, ...'.format(sys.argv[0]))
        
