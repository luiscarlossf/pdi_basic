from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.colorpicker import ColorPicker, ColorWheel
from kivy.uix.dropdown import DropDown

from image_pdi import Image as PI



class TransformProperties(BoxLayout):
    lonsttextinput = ObjectProperty(None)
    gamatextinput = ObjectProperty(None)
    offsettextinput = ObjectProperty(None)
    transformbutton = ObjectProperty(None)
    source = None

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        print("TransformProperties created")
        super(TransformProperties, self).__init__(**kwargs)

    def on_press(self):
        img = self.ui.pdispace.getImage()
        self.ui.processingbar.image_currant = str(img.source)
        ip = PI(filename=self.ui.getSourceImage())
        try:
            offset = float(self.offsettextinput.text)
            newfilename = ip.power(int(self.consttextinput.text), float(self.gamatextinput.text), offset)
        except ValueError:
            newfilename = ip.power(int(self.consttextinput.text), float(self.gamatextinput.text))
        img.source = newfilename
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
        img = self.ui.pdispace.getImage()
        source = str(img.source)
        self.ui.processingbar.image_currant = source
        if self.um.active:
            new = PI(filename=source).fatiamento(1)
            self.ui.pdispace.addImage(new)
        if self.dois.active:
            new = PI(filename=source).fatiamento(2)
            self.ui.pdispace.addImage(new)
        if self.tres.active:
            new = PI(filename=source).fatiamento(3)
            self.ui.pdispace.addImage(new)
        if self.quatro.active:
            new = PI(filename=source).fatiamento(4)
            self.ui.pdispace.addImage(new)
        if self.cinco.active:
            new = PI(filename=source).fatiamento(5)
            self.ui.pdispace.addImage(new)
        if self.seis.active:
            new = PI(filename=source).fatiamento(6)
            self.ui.pdispace.addImage(new)
        if self.sete.active:
            new = PI(filename=source).fatiamento(7)
            self.ui.pdispace.addImage(new)
        if self.oito.active:
            new = PI(filename=source).fatiamento(8)
            self.ui.pdispace.addImage(new)


class HistogramProperties(BoxLayout):
    hist = ObjectProperty(None)
    button = ObjectProperty(None)
    filename = " "

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(HistogramProperties, self).__init__(**kwargs)


    def setHistogram(self, filename):
        try:
            newfilename = PI(filename=filename).histogram()
            self.hist.source = newfilename
            self.hist.reload()
        except AttributeError:
            self.hist.source = " "
            self.hist.reload()


    def get_gcf(self, source):
        plt = PI(filename=source).histogram()
        return plt

    def equalizar(self):
        if self.ui.pdispace.panelimages.content != 'None':
            img = self.ui.pdispace.getImage()
            source = str(img.source)
            self.ui.processingbar.image_currant = source
            new = PI(filename=source).equalize()
            img.source = new
            img.reload()
            self.hist.reload()


class FilterProperties(BoxLayout):
    kernelTextInput = ObjectProperty(None)
    mediana = ObjectProperty(None)
    media = ObjectProperty(None)
    max = ObjectProperty(None)
    min = ObjectProperty(None)
    first = 1
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(FilterProperties, self).__init__(**kwargs)

    def on_press(self):

        img = self.ui.pdispace.getImage()
        source = str(img.source)
        self.ui.processingbar.image_currant = source
        if self.mediana.active:
            print("Mediana")
            new = PI(source).median_filter(int(self.kernelTextInput.text))
        elif self.media.active:
            print("Media")
            new = PI(source).media_filter(int(self.kernelTextInput.text))
        elif self.max.active:
            print("Max")
            new = PI(source).media_filter(int(self.kernelTextInput.text))
        elif self.min.active:
            print("Min")
            new = PI(source).media_filter(int(self.kernelTextInput.text))
        img.source = new
        img.reload()


class DetectionProperties(BoxLayout):
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(DetectionProperties, self).__init__(**kwargs)

    def detectar(self):
        img = self.ui.pdispace.getImage()
        source = str(img.source)
        self.ui.processingbar.image_currant = source
        new = PI(source).contours_canny()
        img.source = new
        img.reload()

class FatColorProperties(BoxLayout):
    colorwheel = ObjectProperty(None)
    corinput = ObjectProperty(None)
    slices = ObjectProperty(None)

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(FatColorProperties, self).__init__(**kwargs)

    def fatia(self):
        img = self.ui.pdispace.getImage()
        source = str(img.source)
        self.ui.processingbar.image_currant = source
        new = PI(source).colorful(self.slices.text)
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
        self.bind(color= self.on_color)
        super(ColorP, self).__init__(**kwargs)

    def on_color(self, instance, value):
        self.cor = str(value)
        self.fat.corinput.text = str(value)