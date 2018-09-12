from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown

from os import path
from kivy.lang.builder import Builder
import cv2 as cv
import ip



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

    def equalizar(self):
        pass

class FilterProperties(BoxLayout):
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(FilterProperties, self).__init__(**kwargs)

class DetectionProperties(BoxLayout):
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(DetectionProperties, self).__init__(**kwargs)

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