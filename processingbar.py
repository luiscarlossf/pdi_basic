from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from properties import DefaultProperties,TransformProperties, BitProperties, HistogramProperties
from properties import DetectionProperties, FatColorProperties, FilterProperties
import ip
import os

class ProcessingBar(BoxLayout):
    ui = ObjectProperty(None)
    image_currant = str()
    p = [DefaultProperties(), TransformProperties(ui=ui), BitProperties(),HistogramProperties(ui=ui), \
         FilterProperties(), DetectionProperties(), FatColorProperties()]

    def addProperties(self, index):
        self.clear_widgets()
        self.p[index].ui = self.ui
        self.add_widget(Label(text='Propriedades', size_hint=(1, 0.2)))
        self.add_widget(self.p[index])
        self.add_widget(RevertButton(self.ui, self, text='Reverter', size_hint=(1, 0.3)))
        self.add_widget(CloseButton(self.ui, text='Fechar Imagem', size_hint=(1, 0.3)))

    # def salveImageCurrant(self):
    #     self.image_currant = image.source


class RevertButton(Button):
    def __init__(self, ui, processingbar,  **kwargs):
        self.pb = processingbar
        self.ui =ui
        super(RevertButton, self).__init__(**kwargs)

    def on_press(self):
        os.remove(self.ui.getSourceImage())
        self.ui.pdispace.setSourceImage(self.pb.image_currant)

class CloseButton(Button):
    def __init__(self, ui,  **kwargs):
        self.ui =ui
        super(CloseButton, self).__init__(**kwargs)

    def on_press(self):
        panelimages = self.ui.pdispace.panelimages
        panelimages.remove_widget(panelimages.content)
        panelimages.remove_widget(panelimages.current_tab)
        panelimages.switch_to(panelimages.tab_list[0],do_scroll=False)
        self.ui.setSourceImage(" ")
