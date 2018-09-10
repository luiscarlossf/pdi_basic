from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from properties import DefaultProperties,TransformProperties, FatiamentoProperties, HistogramProperties
from properties import DetectionProperties, FatColorProperties, FilterProperties
import ip

class ProcessingBar(BoxLayout):
    ui = ObjectProperty(None)
    p = [DefaultProperties(), TransformProperties(ui=ui), FatiamentoProperties(), \
         HistogramProperties(), FilterProperties(), DetectionProperties(), FatColorProperties()]

    def addProperties(self, index):
        self.clear_widgets()
        self.p[index].ui = self.ui
        self.add_widget(Label(text='Propriedades'))
        self.add_widget(self.p[index])

