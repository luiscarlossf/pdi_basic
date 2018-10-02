from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.colorpicker import ColorWheel  # , ColorPicker  # Unused
from kivy.uix.dropdown import DropDown
from image_pdi import ImagePDI


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
            self.ui.pdispace.add_image(new)
        if self.dois.active:
            new = ImagePDI(filename=source).fatiamento(2)
            self.ui.pdispace.add_image(new)
        if self.tres.active:
            new = ImagePDI(filename=source).fatiamento(3)
            self.ui.pdispace.add_image(new)
        if self.quatro.active:
            new = ImagePDI(filename=source).fatiamento(4)
            self.ui.pdispace.add_image(new)
        if self.cinco.active:
            new = ImagePDI(filename=source).fatiamento(5)
            self.ui.pdispace.add_image(new)
        if self.seis.active:
            new = ImagePDI(filename=source).fatiamento(6)
            self.ui.pdispace.add_image(new)
        if self.sete.active:
            new = ImagePDI(filename=source).fatiamento(7)
            self.ui.pdispace.add_image(new)
        if self.oito.active:
            new = ImagePDI(filename=source).fatiamento(8)
            self.ui.pdispace.add_image(new)


class HistogramProperties(BoxLayout):
    hist = ObjectProperty(None)
    button = ObjectProperty(None)
    filename = " "

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(HistogramProperties, self).__init__(**kwargs)

    def setHistogram(self, filename):
        try:
            new_file_name = ImagePDI(filename=filename).histogram()
            self.hist.source = new_file_name
            self.hist.reload()
        except AttributeError:
            self.hist.source = " "
            self.hist.reload()

    def get_gcf(self, source):
        plt = ImagePDI(filename=source).histogram()
        return plt

    def equalizar(self):
        if self.ui.pdi_space.panel_images.content != 'None':
            img = self.ui.pdispace.get_image()
            source = str(img.source)
            self.ui.processingbar.image_currant = source
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
        self.fat.corinput.text = str(value)
