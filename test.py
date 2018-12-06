import cv2 as cv
import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from binaryheap import BinaryHeap
from collections import Counter

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
    a = cv.imread("./images/images_chapter_03/Fig3.08(a).jpg", cv.IMREAD_GRAYSCALE)
    x = const * (((a-a.min())/(a.max() - a.min())) ** gama)
    x = np.array(((a.max() - a.min()) * x) + a.min(), dtype=np.uint8)
    cv.imwrite("./images/temporarias/Fig3.08(a).jpg", x)


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

class TreeLeaf:
    def __init__(self, value):
        self.value = value

class TreeBranch:
    """ Representação do nó interno da arvore de Huffman """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def make_tree(freq_table):
        """ Contrução e retorno da árvore de Huffman
        Montagem da tabela de frequência """

        trees = BinaryHeap()
        trees.insert(TreeLeaf(None), 1)
        for (symbol, freq) in freq_table.items():
            trees.insert(TreeLeaf(symbol), freq)

        while len(trees) > 1:
            right, rfreq = trees.popmin()
            left, lfreq = trees.popmin()
            trees.insert(TreeBranch(left, right), lfreq + rfreq)

        tree, _ = trees.popmin()
        return tree

    def make_encoding_table(huffman_tree):

        table = {}

        def recurse(tree, path):
            """
            Adiciona os valores correspondentes nas folhas
            """
            if isinstance(tree, TreeLeaf):
                table[tree.value] = path
            elif isinstance(tree, TreeBranch):
                recurse(tree.left, path + (False,))
                recurse(tree.right, path + (True,))
            else:
                raise TypeError('{} is not a tree type'.format(type(tree)))

        recurse(huffman_tree, ())
        return table

    def make_freq_table(stream):

        freqs = Counter()
        buffer = bytearray(512)
        while True:
            count = stream.readinto(buffer)
            freqs.update(buffer[:count])
            if count < len(buffer):  # end of stream
                break
        return freqs

if __name__ == '__main__':
    fatiamento(['0,50, 0'])
