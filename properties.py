from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown

from image_pdi import Image as PI

from backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.button import Button

from os import path
from kivy.lang.builder import Builder
import cv2 as cv
import ip

from image_pdi import Image as PI



class TransformProperties(BoxLayout):
    lonsttextinput = ObjectProperty(None)
    gamatextinput = ObjectProperty(None)
    offsettextinput = ObjectProperty(None)
    transformbutton = ObjectProperty(None)
    first = 1
    source = None

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        print("TransformProperties created")
        super(TransformProperties, self).__init__(**kwargs)

    def on_press(self):
        #item=self.panelimages.current_tab
        img = self.ui.pdispace.getImage()
        if (self.first == 1) or not(self.source == img.source):
            self.ui.processingbar.image_currant = img.source
            self.source = img.source
        else:
            self.first +=1
        try:
            offset = float(self.offsettextinput.text)
            ip.power_transform(img.source, int(self.consttextinput.text), float(self.gamatextinput.text), offset)
        except ValueError:
            ip.power_transform(img.source, int(self.consttextinput.text), float(self.gamatextinput.text))
        img.source = "./images/temporarias/"+path.basename(img.source)
        img.reload()

class BitProperties(BoxLayout):
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(BitProperties, self).__init__(**kwargs)

class HistogramProperties(BoxLayout):
    hist = ObjectProperty(None)
    button = ObjectProperty(None)

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(HistogramProperties, self).__init__(**kwargs)


    def get_gcf(self, source):
        plt = PI(filename=source).histogram()
        return plt

    def equalizar(self):
        self.hist = FigureCanvasKivyAgg(self.get_gcf("./images/deadpool.jpg"))
        self.add_widget(self.hist)
        source = self.ui.getSourceImage()
        plt = PI(filename=source).equalize()
        self.hist.figure = plt

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
        source = self.ui.getSourceImage()
        self.ui.processingbar.image_currant = source
        if self.mediana.active:
            print("Mediana")
            new = PI(source).median_filter(int(self.kernelTextInput.text))
            self.ui.setSourceImage(new)
        elif self.media.active:
            print("Media")
            new = PI(source).media_filter(int(self.kernelTextInput.text))
            self.ui.setSourceImage(new)
        elif self.max.active:
            pass
        elif self.min.active:
            pass


class DetectionProperties(BoxLayout):
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(DetectionProperties, self).__init__(**kwargs)

    def detectar(self):
        source = self.ui.getSourceImage()
        self.ui.processingbar.image_currant = source
        new = PI(source).contours_canny()
        self.ui.setSourceImage(new)

class FatColorProperties(BoxLayout):
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(FatColorProperties, self).__init__(**kwargs)

class DefaultProperties(BoxLayout):
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(DefaultProperties, self).__init__(**kwargs)

class CustomDropDown(DropDown):
    pass