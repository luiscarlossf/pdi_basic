import cv2 as cv
import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from image_pdi import Image as PI


class TestApp(App):
    def build(self):
        b = BoxLayout()
        filename = PI(filename="./images/estrada.jpg").media_filter(5)
        # fcka = FigureCanvasKivyAgg(plt)
        b.add_widget(Image(source=filename))
        return b


def binary():
    while (True):
        num = int(input())
        if num == 0:
            break
        num_bin = np.binary_repr(num, 8)
        for i in range(1, 9):
            print(num_bin[8 - i:])

    a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype='uint8')

    p = np.unpackbits(a)
    for i in p:
        print(i)
    print(p)


def get_number(num, level):
    num_text = str(num)
    tamanho = len(str(num))
    num_text = num_text[tamanho - level:tamanho + 1]
    print(num_text)


def bit_plane_slicing():
    a = cv.imread("./")
    b = float(a)
    # tamanho = size(b)

    r = input()


def bit(const, gama):
    a = cv.imread("./images/images_chapter_03/Fig3.08(a).jpg", cv.IMREAD_GRAYSCALE)
    b = a < 0
    x = const * (((a - a.min()) / (a.max() - a.min())) ** gama)
    x = np.array(((a.max() - a.min()) * x) + a.min(), dtype=np.uint8)
    cv.imwrite("./images/temporarias/Fig3.08(a).jpg", x)


def fatiamento(list):
    a = cv.imread("./images/images_chapter_03/Fig3.08(a).jpg", cv.IMREAD_GRAYSCALE)
    rows, cols = a.shape
    for i in range(0, rows):
        for j in range(0, cols):
            for k in list:
                k = k.split(",")
                if a[i][j] > int(k[0]) and a[i][j] <= int(k[1]):
                    a[i][j] = int(k[2])
                else:
                    a[i][j] = 255
    result = cv.cvtColor(a, cv.COLOR_GRAY2RGB)
    cv.imwrite("./images/temporarias/Fig3.08(a).jpg", result)


if __name__ == '__main__':
    fatiamento(['0,50, 0'])
