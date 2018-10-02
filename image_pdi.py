import os

import cv2
import numpy as np
from PIL import ImageFilter, Image
from matplotlib import pyplot as plt


class Image:

    def __init__(self, filename):
        self.image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        self.filename = filename
        self.kernel = np.ones((6, 6), np.float32) / 25  # definição do KERNEL/MÁSCARA

    def print_pixels(self):
        print("Altura: %d pixels" % (self.image.shape[0]))  # shape é um vetor --> índice p extrair o necessario
        print("Largura: %d pixels" % (self.image.shape[1]))
        # print("Canais: %d" % (self.img.shape[2]))

    def set_kernel(self, altura, largura):
        self.kernel = np.ones((altura, largura), np.float32) / 25

    def power(self, const, gama, offset=None):
        a = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
        if offset is None:
            x = const * (((a - a.min()) / (a.max() - a.min())) ** gama)
        else:
            x = const * ((((a + offset) - a.min()) / (a.max() - a.min())) ** gama)
        x = np.array(((a.max() - a.min()) * x) + a.min(), dtype=np.uint8)
        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(newfilename, x)
        return newfilename

    def min_filter(self, kernel):  # aplicar o filtro MINIMO
        im = Image.open(self.filename)
        image = im.filter(ImageFilter.MinFilter(kernel))
        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        image.save(newfilename)
        return newfilename

    def max_filter(self, kernel):  # aplicar o filtro MAXIMO
        im = Image.open(self.filename)
        image = im.filter(ImageFilter.MaxFilter(kernel))
        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        image.save(newfilename)
        return newfilename

    def media_filter(self, size):  # aplicar o filtro da MÉDIA
        blur = cv2.blur(self.image, (size, size))
        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(newfilename, blur)
        return newfilename

    def median_filter(self, size):  # aplicar o filtro da MEDIANA
        # elimina eficientemento o ruído (sal e pimenta)
        if (size % 2 == 0):
            size += 1
        median_blur = cv2.medianBlur(self.image, size)
        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(newfilename, median_blur)
        return newfilename

    def filter2d(self, ddepth=-1):  # CONVOLUÇÃO DISCRETA 2D
        # toma como base a imagem e o valor definido no KERNEL
        image = cv2.imread(self.filename)
        cv2.filter2D(image, ddepth, self.kernel)
        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(newfilename, image)
        return newfilename

    def histogram(self):
        plt.gcf().clear()
        cv2.calcHist(self.image, [0], None, [256], [0, 256])
        plt.hist(self.image.ravel(), 256, [0, 256])
        plt.title('Histograma')
        plt.xlabel('Valores dos pixels')
        plt.ylabel('Qntd. de pixels')
        plt.grid(True)
        newfilename = "./images/temporarias/histogram.jpg"
        try:
            os.remove(newfilename)
        except FileNotFoundError:
            pass
        plt.savefig(newfilename)
        return newfilename

    def histogram_bgr(self):
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histograma = cv2.calcHist([self.image], [i], None, [256], [0, 256])
            plt.plot(histograma, color=col)
            plt.xlim([0, 256])
        plt.title('Histograma: escala BGR')
        plt.xlabel('Valores dos pixels')
        plt.ylabel('Qntd. de pixels')
        plt.grid(True)
        plt.show()

    def contours(self):
        # CONTORNOS - Detector de Bordas
        im = cv2.imread(self.filename)
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        im_o, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # contours --> é uma lista em Python de todos os contornos da imagem (contorno = matriz)
        # Desenhando os CONTORNOS na Imagem:
        img_cont = cv2.drawContours(im, contours, -1, (0, 255, 0), 3)
        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(newfilename, img_cont)
        return newfilename
        # parametros: (imagem_origem, lista_contornos, índice (-1), cor, espessura...)
        # cv2.imwrite("D:\imagem_cont.jpg", img_cont) SALVAR A IMAGEM

    def contours_canny(self):
        # Detecção de contornos pelo MÉTODO CANNY
        image = cv2.imread(self.filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        suave = cv2.GaussianBlur(gray, (7, 7), 0)
        canny = cv2.Canny(suave, 10, 30)  # 20, 120 - menos mais bordas
        result = np.vstack(canny)
        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(newfilename, result)
        return newfilename
        # cv2.imwrite("D:\imagem_bordasCanny.jpg", result) SALVAR A IMAGEM

    def equalize(self):
        # EQUALIZAÇÃO DO HISTOGRAMA --> "esticar" o hist, evitar que fique concentrado apenas em um ponto alto
        # Melhorar o contraste da imagem --> aumentar detalhes
        plt.gcf().clear()
        # self.image = cv2.imread(self.filename, 0)
        # self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        equa = cv2.equalizeHist(src=self.image)
        cv2.calcHist(equa, [0], None, [256], [0, 256])
        plt.hist(equa.ravel(), 256, [0, 256])
        plt.title('Histograma Equalizado')
        plt.xlabel('Valores dos pixels')
        plt.ylabel('Qntd. de pixels')
        plt.grid(True)

        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(newfilename, equa)
        plt.savefig("./images/temporarias/histogram.jpg")
        return newfilename
        # res = np.hstack((img, equa))  # colocar imagem original e equa lado a lado
        # cv2.imwrite("D:\imagem_equalizada.jpg", res)

    def fatiamento(self, plane):
        a = self.image
        # = np.array([[1, 2,3,4],[5,6,7,8]], dtype=np.uint8)
        p = np.array([[int(np.binary_repr(a[i][j], 8)[8 - plane]) * 255 for j in range(0, a.shape[1])] for i in
                      range(0, a.shape[0])])
        cv2.imwrite("./images/temporarias/" + str(plane) + ".jpg", p)
        return "./images/temporarias/" + str(plane) + ".jpg"

    def colorful(self, st):
        st = st.replace(" ", "")
        st = st.replace("(", "")
        st = st.replace(")", "")
        lista = st.split(";")
        a = cv2.imread(self.filename)
        rows, cols, c = a.shape
        for i in range(0, rows):
            for j in range(0, cols):
                for k in lista:
                    e = k.split(",")
                    max = int(e[1])
                    min = int(e[0])
                    if (a[i][j][0] >= min) and (a[i][j][0] <= max):
                        a[i][j] = [int(e[2]), int(e[3]), int(e[4])]
        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(newfilename, a)
        return newfilename


if __name__ == "__main__":
    y = Image("./images/images_chapter_03/Fig3.35(a).jpg")
    y.media_filter(35)
