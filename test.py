import cv2 as cv
import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from image_pdi import ImagePDI as PI



class TestApp(App):
    @staticmethod
    def build():
        b = BoxLayout()
        filename = PI(filename="./images/estrada.jpg").media_filter(5)
        b.add_widget(Image(source=filename))
        return b


def binary():
    while True:
        num = int(input())
        if num == 0:
            break
        num_bin = np.binary_repr(num, 8)
        for i in range(1, 9):
            print(num_bin[8-i:])

    a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype='uint8')
    p = np.unpackbits(a)
    for i in p:
        print(i)
    print(p)


def get_number(num, level):
    num_text = str(num)
    tamanho = len(str(num))
    num_text = num_text[tamanho-level:tamanho+1]
    print(num_text)

def bit(const, gama):
<<<<<<< HEAD
    a = cv.imread("./images/estrada.jpg", cv.IMREAD_GRAYSCALE)
    # = np.array([[1, 2,3,4],[5,6,7,8]], dtype=np.uint8)
    p1 = np.array([[int(np.binary_repr(a[i][j], 8)[7]) * 255  for j in range(0, a.shape[1])] for i in range(0,a.shape[0])])
    cv.imwrite("./images/temporarias/1.jpg", p1)
    p2 = np.array([[int(np.binary_repr(a[i][j], 8)[6]) * 255 for j in range(0, a.shape[1])] for i in range(0, a.shape[0])])
    cv.imwrite("./images/temporarias/2.jpg", p2)
    p3 = np.array([[int(np.binary_repr(a[i][j], 8)[5]) * 255 for j in range(0, a.shape[1])] for i in range(0, a.shape[0])])
    cv.imwrite("./images/temporarias/3.jpg", p3)
    p4 = np.array([[int(np.binary_repr(a[i][j], 8)[4]) * 255 for j in range(0, a.shape[1])] for i in range(0, a.shape[0])])
    cv.imwrite("./images/temporarias/4.jpg", p4)
    p5 = np.array([[int(np.binary_repr(a[i][j], 8)[3]) * 255 for j in range(0, a.shape[1])] for i in range(0, a.shape[0])])
    cv.imwrite("./images/temporarias/5.jpg", p5)
    p6 = np.array([[int(np.binary_repr(a[i][j], 8)[2]) * 255 for j in range(0, a.shape[1])] for i in range(0, a.shape[0])])
    cv.imwrite("./images/temporarias/6.jpg", p6)
    p7 = np.array([[int(np.binary_repr(a[i][j], 8)[1]) * 255 for j in range(0, a.shape[1])] for i in range(0, a.shape[0])])
    cv.imwrite("./images/temporarias/7.jpg", p7)
    p8 = np.array([[int(np.binary_repr(a[i][j], 8)[0]) * 255 for j in range(0, a.shape[1])] for i in range(0, a.shape[0])])
    cv.imwrite("./images/temporarias/8.jpg", p8)

    print("--------------------------------------------------")
    print(p1)

=======
    a = cv.imread("./images/images_chapter_03/Fig3.08(a).jpg", cv.IMREAD_GRAYSCALE)
    x = const * (((a-a.min())/(a.max() - a.min())) ** gama)
    x = np.array(((a.max() - a.min()) * x) + a.min(), dtype=np.uint8)
    cv.imwrite("./images/temporarias/Fig3.08(a).jpg", x)
>>>>>>> 7a5d610ca2f1b1992e6ca283aa6ed7dad276d45a


def fatiamento(list):
    a = cv.imread(
        "./images/images_chapter_03/Fig3.08(a).jpg", cv.IMREAD_GRAYSCALE)
    rows, cols = a.shape
    for i in range(0, rows):
        for j in range(0, cols):
            for k in list:
                k = k.split(",")
                if int(k[0]) < a[i][j] <= int(k[1]):
                    a[i][j] = int(k[2])
                else:
                    a[i][j] = 255
    result = cv.cvtColor(a, cv.COLOR_GRAY2RGB)
    cv.imwrite("./images/temporarias/Fig3.08(a).jpg", result)
"""
Parameters
----------
image : ndarray
    Input image data. Will be converted to float.
mode : str
    One of the following strings, selecting the type of noise to add:

    'gauss'     Gaussian-distributed additive noise.
    'poisson'   Poisson-distributed noise generated from the data.
    's&p'       Replaces random pixels with 0 or 1.
    'speckle'   Multiplicative noise using out = image + n*image,where
                n is uniform noise with specified mean & variance.
"""
def noisy(noise_typ,image):
   if noise_typ == "gauss":
      row,col,ch= image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy

   elif noise_typ == "s&p":
      row,col,ch = image.shape
      s_vs_p = 0.5
      amount = 0.004
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
      out[coords] = 1

      # Pepper mode
      num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0
      return out

   elif noise_typ == "poisson":
      vals = len(np.unique(image))
      vals = 2 ** np.ceil(np.log2(vals))
      noisy = np.random.poisson(image * vals) / float(vals)
      return noisy

   elif noise_typ =="speckle":
      row,col,ch = image.shape
      gauss = np.random.randn(row,col,ch)
      gauss = gauss.reshape(row,col,ch)
      noisy = image + image * gauss
      return noisy


if __name__ == '__main__':
    fatiamento(['0,50, 0'])
