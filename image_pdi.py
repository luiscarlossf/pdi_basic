import os

import cv2
import numpy as np
from PIL import ImageFilter, Image as img
from matplotlib import pyplot as plt
from scipy import ndimage



class ImagePDI:
    def __init__(self, filename):
        self.image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        self.filename = filename
        # definição do KERNEL/MÁSCARA
        self.kernel = np.ones((6, 6), np.float32) / 25

    def print_pixels(self):
        # shape é um vetor --> índice p extrair o necessario
        print("Altura: %d pixels" % (self.image.shape[0]))
        print("Largura: %d pixels" % (self.image.shape[1]))

    def set_kernel(self, altura, largura):
        self.kernel = np.ones((altura, largura), np.float32) / 25

    def power(self, const, gama, offset=None):
        a = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
        if offset is None:
            x = const * (((a - a.min()) / (a.max() - a.min())) ** gama)
        else:
            x = const *\
             ((((a + offset) - a.min()) / (a.max() - a.min())) ** gama)
        x = np.array(((a.max() - a.min()) * x) + a.min(), dtype=np.uint8)
        newfilename = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(newfilename, x)
        return newfilename

    def min_filter(self, kernel):  # aplicar o filtro MINIMO
        im = img.open(self.filename)
        image = im.filter(ImageFilter.MinFilter(kernel))
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        image.save(new_file_name)
        return new_file_name

    def max_filter(self, kernel):  # aplicar o filtro MAXIMO
        im = img.open(self.filename)
        image = im.filter(ImageFilter.MaxFilter(kernel))
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        image.save(new_file_name)
        return new_file_name

    def media_filter(self, size):  # aplicar o filtro da MÉDIA
        blur = cv2.blur(self.image, (size, size))
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(new_file_name, blur)
        return new_file_name

    def median_filter(self, size):  # aplicar o filtro da MEDIANA
        # elimina eficientemento o ruído (sal e pimenta)
        if(size % 2 == 0):
            size += 1
        median_blur = cv2.medianBlur(self.image, size)
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(new_file_name, median_blur)
        return new_file_name

    def geometric_filter(self, kernel):
        pass

    def alpha_filter(self, kernel):
        pass

    def filter2d(self, ddepth=-1):  # CONVOLUÇÃO DISCRETA 2D
        # toma como base a imagem e o valor definido no KERNEL
        image = cv2.imread(self.filename)
        cv2.filter2D(image, ddepth, self.kernel)
        new_file_name = "./images/temporarias/"+os.path.basename(self.filename)
        cv2.imwrite(new_file_name, image)
        return new_file_name

    def histogram(self):
        plt.gcf().clear()
        cv2.calcHist(self.image, [0], None, [256], [0, 256])
        plt.hist(self.image.ravel(), 256, [0, 256])
        plt.title('Histograma')
        plt.xlabel('Valores dos pixels')
        plt.ylabel('Qntd. de pixels')
        plt.grid(True)
        new_file_name = "./images/temporarias/histogram.jpg"
        try:
            os.remove(new_file_name)
        except FileNotFoundError:
            pass
        plt.savefig(new_file_name)
        return new_file_name

    def histogram_bgr(self):
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histogram = cv2.calcHist([self.image], [i], None, [256], [0, 256])
            plt.plot(histogram, color=col)
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
        im_o, contours, hierarchy = cv2.findContours(
                                  thresh,
                                  cv2.RETR_TREE,
                                  cv2.CHAIN_APPROX_SIMPLE)
        # contours --> é uma lista em Python de
        # todos os contornos da imagem (contorno = matriz)
        # Desenhando os CONTORNOS na Imagem:
        img_cont = cv2.drawContours(im, contours, -1, (0, 255, 0), 3)
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(new_file_name, img_cont)
        return new_file_name
        # parametros: (imagem_origem, lista_contornos,
        # índice (-1), cor, espessura...)
        # cv2.imwrite("D:\imagem_cont.jpg", img_cont) SALVAR A IMAGEM

    def contours_canny(self):
        # Detecção de contornos pelo MÉTODO CANNY
        image = cv2.imread(self.filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        suave = cv2.GaussianBlur(gray, (7, 7), 0)
        canny = cv2.Canny(suave, 10, 30)  # 20, 120 - menos mais bordas
        result = np.vstack(canny)
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(new_file_name, result)
        return new_file_name
        # cv2.imwrite("D:\imagem_bordasCanny.jpg", result) SALVAR A IMAGEM

    def equalize(self):
        # EQUALIZAÇÃO DO HISTOGRAMA --> "esticar" o hist,
        # evitar que fique concentrado apenas em um ponto alto
        # Melhorar o contraste da imagem --> aumentar detalhes
        plt.gcf().clear()
        equa = cv2.equalizeHist(src=self.image)
        cv2.calcHist(equa, [0], None, [256], [0, 256])
        plt.hist(equa.ravel(), 256, [0, 256])
        plt.title('Histograma Equalizado')
        plt.xlabel('Valores dos pixels')
        plt.ylabel('Qntd. de pixels')
        plt.grid(True)

        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(new_file_name, equa)
        plt.savefig("./images/temporarias/histogram.jpg")
        return new_file_name
        # res = np.hstack((img, equa)) 
        #colocar imagem original e equa lado a lado
        # cv2.imwrite("D:\imagem_equalizada.jpg", res)

    def fatiamento(self, plane):
        a = self.image
        # = np.array([[1, 2,3,4],[5,6,7,8]], dtype=np.uint8)
        p = np.array(
                     [[int(np.binary_repr(a[i][j], 8)[8 - plane]) * 255
                       for j in range(0, a.shape[1])]
                      for i in range(0, a.shape[0])])
        cv2.imwrite("./images/temporarias/"+str(plane)+".jpg", p)
        return "./images/temporarias/"+str(plane)+".jpg"

    def colorful(self, st):
        st = st.replace(" ", "")
        st = st.replace("(", "")
        st = st.replace(")", "")
        list_of_strings = st.split(";")
        a = cv2.imread(self.filename)
        rows, cols, c = a.shape
        for i in range(0, rows):
            for j in range(0, cols):
                for k in list_of_strings:
                    e = k.split(",")
                    max_value = int(e[1])
                    min_value = int(e[0])
                    if (a[i][j][0] >= min_value) and (a[i][j][0] <= max_value):
                        a[i][j] = [int(e[2]), int(e[3]), int(e[4])]
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(new_file_name, a)
        return new_file_name

    def gaussian_noise(self):
        row,col= self.image.shape
        mean = 0
        var = 0.1
        sigma = var**0.5
        gauss = np.random.normal(mean,sigma,(row,col))
        gauss = gauss.reshape(row,col)
        noisy = self.image + gauss
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(new_file_name, noisy)
        return new_file_name

    def pepper_salt_noise(self):
        row,col= self.image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(self.image)
        # Salt mode
        num_salt = np.ceil(amount * self.image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in self.image.shape]
        out[coords] = 255

        # Pepper mode
        num_pepper = np.ceil(amount* self.image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in self.image.shape]
        out[coords] = 0
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(new_file_name, out)
        return new_file_name

    def erosion(self, tam, type_es):
        kernel = self.generate_es(tam, type_es)
        e = cv2.erode(self.image, kernel, iterations=1)
        cv2.imshow("Erosao", e)
        cv2.waitKey(5000)
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(new_file_name, e)
        return new_file_name

    def dilatation(self, tam, type_es):
        """ Método para realizar a dilatação na imagem
        Efeitos: aumentar partículas,
        preencher buracos,
        conectar componentes próximos """

        kernel = self.generate_es(tam, type_es)
        #   kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        #   kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        #   kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

        d = cv2.dilate(self.image, kernel, iterations=1)
        cv2.imshow("Dilatacao", d)
        cv2.waitKey(5000)
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(new_file_name, d)
        return new_file_name

    def opening(self, tam, type_es):
        """ Método para realizar a abertura da imagem
        A abertura elimina pequenos componentes e suaviza o contorno
        Efeitos: separa componentes,
        elimina pequenos componentes """

        kernel = self.generate_es(tam, type_es)
        #   kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        #   kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        #   kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

        o = cv2.morphologyEx(self.image, cv2.MORPH_OPEN, kernel)
        cv2.imshow("Abertura", o)
        cv2.waitKey(5000)
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(new_file_name, o)
        return new_file_name

    def closing(self, tam, type_es):
        """ Método para realizar o fechamento da imagem
        O fechamento fecha pequenos buracos e conecta componentes
        Efeitos:  Preenche buracos no interior dos componentes,
        conecta componentes próximos """
        kernel = self.generate_es(tam, type_es)
        #   kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        #   kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        #   kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        c = cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, kernel)
        cv2.imshow("Fechamento", c)
        cv2.waitKey(5000)
        new_file_name = "./images/temporarias/" + os.path.basename(self.filename)
        cv2.imwrite(new_file_name, c)
        return new_file_name

    def region_growing(self):
        pass

    def huffman(self):
        pass

    def generate_es(self, tam, type_es):
        if type_es  == 1:
            pass
        elif type_es == 2:
            pass
        elif type_es == 3:
            pass
        elif type_es == 4:
            pass
        elif type_es == 5:
            pass
        elif type_es == 6:
            a = np.ones((tam, tam), np.uint8)
            return a
        elif type_es == 7:
            a = np.ones((tam, tam), np.uint8)
            return a

if __name__=="__main__":
    y = ImagePDI("./images/images_chapter_03/Fig3.35(a).jpg")
    y.media_filter(35)


