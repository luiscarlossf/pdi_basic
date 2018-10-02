# File name: pdispace.py

from os import path

from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.tabbedpanel import TabbedPanelHeader


class PdiSpace(BoxLayout):
    ui = ObjectProperty(None)
    panelimages = ObjectProperty(None)
    filename = "Bem vindo!"

    # Retorna a Image Object corrente no panel de imagens
    def get_image(self):
        image = self.panelimages.current_tab.content
        return image

    # Modifica a image corrente no panel de imagens
    def set_source_image(self, source):
        self.panelimages.current_tab.content.source = source

    # Adiciona uma nova imagem, ou novo item, no panel de images
    def add_image(self, filename):
        self.filename = filename
        item = PDIHeader(ui=self.ui, text=path.basename(filename))
        item.content = Image(source=filename)
        self.panelimages.add_widget(item)
        self.panelimages.switch_to(item)
        self.ui.statusbar.labelright.text = self.filename
        self.ui.processingbar.set_histogram(filename)


class PropertyGroup(BoxLayout):
    pass


class PDIHeader(TabbedPanelHeader, Button):

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(PDIHeader, self).__init__(**kwargs)

    def on_press(self):
        source = str(self.content.source)
        self.ui.statusbar.labelright.text = source
        self.ui.processingbar.set_histogram(source)
