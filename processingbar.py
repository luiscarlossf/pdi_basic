from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from properties import DefaultProperties,TransformProperties, FatiamentoProperties, HistogramProperties
from properties import DetectionProperties, FatColorProperties, FilterProperties
import ip

class ProcessingBar(BoxLayout):
    ui = ObjectProperty(None)
    image_currant = str()
    p = [DefaultProperties(), TransformProperties(ui=ui), FatiamentoProperties(), \
         HistogramProperties(), FilterProperties(), DetectionProperties(), FatColorProperties()]

    def addProperties(self, index):
        self.clear_widgets()
        self.p[index].ui = self.ui
        self.add_widget(Label(text='Propriedades'))
        self.add_widget(self.p[index])
        self.add_widget(RevertButton(text='Reverter Imagem'))

    def applyOperation(self, widget):
        image = self.ui.pdispace.getImage()
        self.image_currant = image.source

class RevertButton(Button):
    def __init__(self, processingbar,  **kwargs):
        self.pb = processingbar
        super(RevertButton, self).__init__(**kwargs)

    def on_press(self):
        self.ui.pdispace.setImage(self.pb.image_currant)
