from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from os import path
from kivy.lang.builder import Builder
import ip



class TransformProperties(BoxLayout):
    lonsttextinput = ObjectProperty(None)
    gamatextinput = ObjectProperty(None)
    offsettextinput = ObjectProperty(None)
    transformbutton = ObjectProperty(None)

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        print("TransformProperties created")
        super(TransformProperties, self).__init__(**kwargs)

    def on_press(self):
        #item=self.panelimages.current_tab
        image = self.ui.pdispace.getImage()
        ip.power_transform(image.source, int(self.consttextinput.text), float(self.gamatextinput.text))
        image.source = "./images/temporarias/"+path.basename(image.source)
        image.reload()

class FatiamentoProperties(BoxLayout):
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(FatiamentoProperties, self).__init__(**kwargs)

class HistogramProperties(BoxLayout):
    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(HistogramProperties, self).__init__(**kwargs)

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