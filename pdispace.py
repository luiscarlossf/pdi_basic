#File name: pdispace.py

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.tabbedpanel import TabbedPanelItem, TabbedPanelContent, TabbedPanelHeader
from kivy.uix.image import Image
from kivy.uix.label import Label
from properties import TransformProperties
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from cv2 import imread,imshow
import ip

from os import path

class PdiSpace(BoxLayout):
    ui = ObjectProperty(None)
    panelimages = ObjectProperty(None)
    filename = "Bem vindo!"

    #Retorna a Image Object corrente no panel de imagens
    def getImage(self):
        return self.panelimages.current_tab.content

    #Modifica a image corrente no panel de imagens
    def setSourceImage(self, source):
        self.panelimages.current_tab.content.source = source

    #Adiciona uma nova imagem, ou novo item, no panel de images
    def addImage(self, filename):
        self.filename = filename
        item = TabbedPanelHeader(text= path.basename(filename))
        item.content = Image(source=filename)
        self.panelimages.add_widget(item)
        self.ui.statusbar.labelright.text = self.filename

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.ui.statusbar.labelright.text = self.getImage().source
        return super(PdiSpace, self).on_touch_down(touch)

class propertyGroup(BoxLayout):
    pass


