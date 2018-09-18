#File name: pdispace.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import  TabbedPanelHeader
from kivy.uix.image import Image
from kivy.uix.button import Button

from os import path

class PdiSpace(BoxLayout):
    ui = ObjectProperty(None)
    panelimages = ObjectProperty(None)
    filename = "Bem vindo!"

    #Retorna a Image Object corrente no panel de imagens
    def getImage(self):
        image = self.panelimages.current_tab.content
        return image

    #Modifica a image corrente no panel de imagens
    def setSourceImage(self, source):
        self.panelimages.current_tab.content.source = source

    #Adiciona uma nova imagem, ou novo item, no panel de images
    def addImage(self, filename):
        self.filename = filename
        item = PDIHeader(ui=self.ui, text= path.basename(filename))
        item.content = Image(source=filename)
        self.panelimages.add_widget(item)
        self.panelimages.switch_to(item)
        self.ui.statusbar.labelright.text = self.filename
        self.ui.processingbar.setHistogram(filename)

class propertyGroup(BoxLayout):
    pass

class PDIHeader(TabbedPanelHeader, Button):

    def __init__(self, ui=None, **kwargs):
        self.ui = ui
        super(PDIHeader, self).__init__(**kwargs)

    def on_press(self):
        source = str(self.content.source)
        self.ui.statusbar.labelright.text = source
        self.ui.processingbar.setHistogram(source)




