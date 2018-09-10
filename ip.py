from cv2 import imread,imwrite
from cv2 import IMREAD_GRAYSCALE
from os import path


def power_transform(filename, const, gama, offset = None):
    img = imread(filename, IMREAD_GRAYSCALE)
    rows, cols = img.shape
    for i in range(0, rows):
        for j in range(0, cols):
            if offset == None:
                img[i][j] = const * (img[i][j] ** gama)
            else:
                img[i][j] = const * ((img[i][j] + offset)** gama)
    imwrite('./images/temporarias/'+path.basename(filename), img)

if __name__=="__main__":
    power_transform('./images/estrada.jpg', 1, 0.1)
