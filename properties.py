from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.colorpicker import ColorWheel  # , ColorPicker  # Unused
from kivy.uix.dropdown import DropDown
from image_pdi import ImagePDI
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import numpy as np
from scipy import ndimage

class TransformProperties(BoxLayout):
    lonst_text_input = ObjectProperty(None)
    gama_text_input = ObjectProperty(None)
    offset_text_input = ObjectProperty(None)
    transform_button = ObjectProperty(None)
    source = None

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        print("TransformProperties created")
        super(TransformProperties, self).__init__(**kwargs)

    def on_press(self):
        img = self.ui.pdi_space.get_image()
        self.ui.processing_bar.image_currant = str(img.source)
        ip = ImagePDI(filename=self.ui.get_source_image())
        try:
            offset = float(self.offset_text_input.text)
            new_file_name = ip.power(int(self.const_text_input.text), float(self.gama_text_input.text), offset)
        except ValueError:
            new_file_name = ip.power(int(self.const_text_input.text), float(self.gama_text_input.text))
        img.source = new_file_name
        img.reload()


class BitProperties(BoxLayout):
    um = ObjectProperty(None)
    dois = ObjectProperty(None)
    tres = ObjectProperty(None)
    quatro = ObjectProperty(None)
    cinco = ObjectProperty(None)
    seis = ObjectProperty(None)
    sete = ObjectProperty(None)
    oito = ObjectProperty(None)

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        self.lista = list()
        super(BitProperties, self).__init__(**kwargs)

    def show_planes(self):
        img = self.ui.pdi_space.get_image()
        source = str(img.source)
        self.ui.processing_bar.image_currant = source
        if self.um.active:
            new = ImagePDI(filename=source).fatiamento(1)
            self.ui.pdi_space.add_image(new)
        if self.dois.active:
            new = ImagePDI(filename=source).fatiamento(2)
            self.ui.pdi_space.add_image(new)
        if self.tres.active:
            new = ImagePDI(filename=source).fatiamento(3)
            self.ui.pdi_space.add_image(new)
        if self.quatro.active:
            new = ImagePDI(filename=source).fatiamento(4)
            self.ui.pdi_space.add_image(new)
        if self.cinco.active:
            new = ImagePDI(filename=source).fatiamento(5)
            self.ui.pdi_space.add_image(new)
        if self.seis.active:
            new = ImagePDI(filename=source).fatiamento(6)
            self.ui.pdi_space.add_image(new)
        if self.sete.active:
            new = ImagePDI(filename=source).fatiamento(7)
            self.ui.pdi_space.add_image(new)
        if self.oito.active:
            new = ImagePDI(filename=source).fatiamento(8)
            self.ui.pdi_space.add_image(new)


class HistogramProperties(BoxLayout):
    hist = ObjectProperty(None)
    button = ObjectProperty(None)
    filename = " "

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(HistogramProperties, self).__init__(**kwargs)

    def set_histogram(self, filename):
        try:
            new_file_name = ImagePDI(filename=filename).histogram()
            self.hist.source = new_file_name
            self.hist.reload()
        except AttributeError:
            self.hist.source = ' '
            self.hist.reload()

    def get_gcf(self, source):
        plt = ImagePDI(filename=source).histogram()
        return plt

    def equalizar(self):
        if self.ui.pdi_space.panel_images.content != 'None':
            img = self.ui.pdi_space.get_image()
            source = str(img.source)
            self.ui.processing_bar.image_currant = source
            new = ImagePDI(filename=source).equalize()
            img.source = new
            img.reload()
            self.hist.reload()


class FilterProperties(BoxLayout):
    kernel_text_input = ObjectProperty(None)
    mediana = ObjectProperty(None)
    media = ObjectProperty(None)
    max = ObjectProperty(None)
    min = ObjectProperty(None)
    geometric = ObjectProperty(None)
    alfa = ObjectProperty(None)
    first = 1

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(FilterProperties, self).__init__(**kwargs)

    def on_press(self):
        img = self.ui.pdi_space.get_image()
        source = str(img.source)
        self.ui.processing_bar.image_currant = source
        new = None
        if self.mediana.active:
            print("Mediana")
            new = ImagePDI(source).median_filter(int(self.kernel_text_input.text))
        elif self.media.active:
            print("Media")
            new = ImagePDI(source).media_filter(int(self.kernel_text_input.text))
        elif self.max.active:
            print("Max")
            new = ImagePDI(source).media_filter(int(self.kernel_text_input.text))
        elif self.min.active:
            print("Min")
            new = ImagePDI(source).media_filter(int(self.kernel_text_input.text))
        elif self.geometric.active:
            print("Geometric")
            new = ImagePDI(source).geometric_filter(int(self.kernel_text_input.text))
        elif self.alfa.active:
            print("Alfa Cortada")
            new = ImagePDI(source).alpha_filter(int(self.kernel_text_input.text))

        img.source = new
        img.reload()


class DetectionProperties(BoxLayout):
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(DetectionProperties, self).__init__(**kwargs)

    def detectar(self):
        img = self.ui.pdi_space.get_image()
        source = str(img.source)
        self.ui.processing_bar.image_currant = source
        new = ImagePDI(source).contours_canny()
        img.source = new
        img.reload()


class FatColorProperties(BoxLayout):
    color_wheel = ObjectProperty(None)
    cor_input = ObjectProperty(None)
    slices = ObjectProperty(None)

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(FatColorProperties, self).__init__(**kwargs)

    def fatia(self):
        img = self.ui.pdi_space.get_image()
        source = str(img.source)
        self.ui.processing_bar.image_currant = source
        new = ImagePDI(source).colorful(self.slices.text)
        img.source = new
        img.reload()


class DefaultProperties(BoxLayout):
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(DefaultProperties, self).__init__(**kwargs)


class CustomDropDown(DropDown):
    pass


class ColorP(ColorWheel):
    cor = ""
    fat = ObjectProperty(None)

    def __init__(self, **kwargs):
        self.bind(color=self.on_color)
        super(ColorP, self).__init__(**kwargs)

    def on_color(self, instance, value):
        self.cor = str(value)
        self.fat.cor_input.text = str(value)

class NoiseProperties(BoxLayout):
    text_input_kernel = ObjectProperty(None)
    gaussian = ObjectProperty(None)
    pepper_salt = ObjectProperty(None)

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(NoiseProperties, self).__init__(**kwargs)

    def on_press(self):
        img = self.ui.pdi_space.get_image()
        source = str(img.source)
        self.ui.processing_bar.image_currant = source
        new = None
        if self.gaussian.active:
            print("Gaussian Noise")
            new = ImagePDI(source).gaussian_noise()
        elif self.pepper_salt.active:
            print("Pepper and Salt Noise")
            new = ImagePDI(source).pepper_salt_noise()
        img.source = new
        img.reload()

class MorphProperties(BoxLayout):
    es_name = ObjectProperty(None)
    es_button = ObjectProperty(None)
    erosion = ObjectProperty(None)
    dilatation = ObjectProperty(None)
    opening = ObjectProperty(None)
    closing = ObjectProperty(None)

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        self.tam = None
        self.type_es = None
        self._popup = None
        super(MorphProperties, self).__init__(**kwargs)

    def on_press(self):
        img = self.ui.pdi_space.get_image()
        source = str(img.source)
        self.ui.processing_bar.image_currant = source
        new = None
        if self.erosion.active:
            print("Erosion")
            new = ImagePDI(source).erosion(self.tam, self.type_es)
        elif self.dilatation.active:
            print("Dilatação")
            new = ImagePDI(source).dilatation(self.tam, self.type_es)
        elif self.opening.active:
            print("Abertura")
            new = ImagePDI(source).opening(self.tam, self.type_es)
        elif self.closing.active:
            print("Fechamento")
            new = ImagePDI(source).closing(self.tam, self.type_es)

        img.source = new
        img.reload()

    def selection_es(self):
        content = ESDialog(select=self.select, cancel=self.dismiss_popup)
        self._popup = Popup(title="Select Element Structure", content=content,
                        size_hint=(0.9, 0.9))
        self._popup.open()

    def select(self, tamanho, type_es):
        self.tam = int(tamanho)
        self.type_es = int(type_es) + 1
        print("Selecionado: ", self.tam, "-", type_es)
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()


class ESDialog(FloatLayout):
    select = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SegmentationProperties(BoxLayout):
    seed = "Nenhuma semente selecionada"

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(SegmentationProperties, self).__init__(**kwargs)


class CompressProperties(BoxLayout):
    pass
