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
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        self.lista = list()
        super(BitProperties, self).__init__(**kwargs)

    def on_press(self):
        pass

class HistogramProperties(BoxLayout):
    hist = ObjectProperty(None)
    button = ObjectProperty(None)
    filename = " "

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(HistogramProperties, self).__init__(**kwargs)


    def setHistogram(self):
        newfilename = PI(filename=self.ui.pdispace.getImage().source).histogram()
        self.hist.source = newfilename
        self.hist.reload()


    def get_gcf(self, source):
        plt = PI(filename=source).histogram()
        return plt

    def equalizar(self):
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
        s = self.slices.text.split(";")

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