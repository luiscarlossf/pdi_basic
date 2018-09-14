import cv2
from matplotlib import pyplot as plt
import numpy as np
import os

class Image:

    def __init__(self, filename):
        self.image = cv2.imread(filename)
        self.filename = filename
        self.kernel = np.ones((6, 6), np.float32) / 25  # definição do KERNEL/MÁSCARA

    def print_pixels(self):
        print("Altura: %d pixels" % (self.image.shape[0]))  # shape é um vetor --> índice p extrair o necessario
        print("Largura: %d pixels" % (self.image.shape[1]))
        # print("Canais: %d" % (self.img.shape[2]))

    def setKernel(self, altura, largura):
        self.kernel = np.ones((altura, largura), np.float32) / 25

    def media_filter(self, size):  # aplicar o filtro da MÉDIA
        image = cv2.imread(self.filename)
        cv2.blur(image, (size, size))
        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(newfilename, self.image)
        return newfilename


    def median_filter(self, size):  # aplicar o filtro da MEDIANA
        # elimina eficientemento o ruído (sal e pimenta)
        image = cv2.imread(self.filename)
        if(size%2 == 0):
            size += 1
        cv2.medianBlur(self.image, size)
        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(newfilename, self.image)
        return newfilename

    def filter2d(self, ddepth = -1):  # CONVOLUÇÃO DISCRETA 2D
        # toma como base a imagem e o valor definido no KERNEL
        image = cv2.imread(self.filename)
        cv2.filter2D(image, ddepth, self.kernel)
        newfilename = "./images/temporarias/"+os.path.basename(self.filename)
        cv2.imwrite(newfilename, image)
        return newfilename

    def histogram(self):
        cv2.calcHist(self.image, [0], None, [256], [0, 256])
        plt.hist(self.image.ravel(), 256, [0, 256])
        plt.title('Histograma')
        plt.xlabel('Valores dos pixels')
        plt.ylabel('Qntd. de pixels')
        plt.grid(True)

        return plt.gcf()

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
        equa = cv2.equalizeHist(images=self.image)
        cv2.calcHist(equa, [0], None, [256], [0, 256])
        plt.hist(equa.ravel(), 256, [0, 256])
        plt.title('Histograma Equalizado')
        plt.xlabel('Valores dos pixels')
        plt.ylabel('Qntd. de pixels')
        plt.grid(True)
        return plt.gcf()
        # res = np.hstack((img, equa))  # colocar imagem original e equa lado a lado
        # cv2.imwrite("D:\imagem_equalizada.jpg", res)
