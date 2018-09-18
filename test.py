from image_pdi import Image as PI
import numpy as np
from kivy.uix.image import Image

import cv2 as cv
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):
    def build(self):
        b = BoxLayout()
        filename = PI(filename="./images/estrada.jpg").media_filter(5)
        #fcka = FigureCanvasKivyAgg(plt)
        b.add_widget(Image(source=filename))
        return b

def binary():
    while(True):
        num = int(input())
        if num ==0:
            break;
        num_bin = np.binary_repr(num, 8)
        for i in range(1, 9):
            print(num_bin[8-i:])

    a = np.array([[1, 2, 3, 4,5], [6,7,8,9,10]], dtype='uint8')

    p = np.unpackbits(a)
    for i in p:
        print(i)
    print(p)

def get_number(num, level):
    num_text = str(num)
    tamanho = len(str(num))
    num_text = num_text[tamanho-level:tamanho+1]
    print(num_text)

def bit_plane_slicing():
    a = cv.imread("./")
    b = float(a)
    #tamanho = size(b)

    r = input()

def bit(const, gama):
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


if __name__=='__main__':
    bit(1, 0.3)

