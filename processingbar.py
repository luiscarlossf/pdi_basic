from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.button import Button
from properties import DefaultProperties, TransformProperties, BitProperties,\
    HistogramProperties
from properties import DetectionProperties, FatColorProperties,\
    FilterProperties
# import os  # Unused


class ProcessingBar(BoxLayout):
    ui = ObjectProperty(None)
    image_currant = str()
    index = -1
    p = [DefaultProperties(), TransformProperties(ui=ui),
         BitProperties(), HistogramProperties(ui=ui),
         FilterProperties(), DetectionProperties(), FatColorProperties()]

    def addProperties(self, index):
        self.index = index
        self.clear_widgets()
        self.p[index].ui = self.ui
        self.add_widget(Label(text='Propriedades', size_hint=(1, 0.2)))
        self.add_widget(self.p[index])
        self.add_widget(RevertButton(
            self.ui, self, text='Reverter', size_hint=(1, 0.3)))
        self.add_widget(CloseButton(
            self.ui, text='Fechar Imagem', size_hint=(1, 0.3)))
        try:
            self.setHistogram(self.ui.pdispace.getImage().source)
        except AttributeError:
            pass

    def setHistogram(self, filename):
        if self.index == 3:
            self.p[self.index].setHistogram(filename)
            self.p[self.index].hist.reload()

    # def salveImageCurrant(self):
    #     self.image_currant = image.source


class RevertButton(Button):
    def __init__(self, ui, processingbar,  **kwargs):
        self.pb = processingbar
        self.ui = ui
        super(RevertButton, self).__init__(**kwargs)

    def on_press(self):
        self.ui.pdispace.setSourceImage(self.pb.image_currant)
        self.ui.pdispace.getImage().reload()
        self.ui.processingbar.setHistogram(self.pb.image_currant)


class CloseButton(Button):
    def __init__(self, ui,  **kwargs):
        self.ui = ui
        super(CloseButton, self).__init__(**kwargs)

    def on_press(self):
        panelimages = self.ui.pdispace.panelimages
        panelimages.content.source = " "
        panelimages.remove_widget(panelimages.content)
        panelimages.remove_widget(panelimages.current_tab)
        try:
            panelimages.switch_to(panelimages.tab_list[0], do_scroll=False)
        except IndexError:
            panelimages.clear_widgets()
