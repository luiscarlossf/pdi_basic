#File name: pdiApp.py
import kivy
kivy.require("1.10.0")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

Builder.load_file('properties.kv')


class Pdi(BoxLayout):
    """
     A classe Pdi define a estrutura e organização dos elementos da interface da aplicação
    """
    menubar = ObjectProperty(None)
    toolbar = ObjectProperty(None)
    pdispace = ObjectProperty(None)
    processingbar = ObjectProperty(None)
    statusbar = ObjectProperty(None)

    def getImage(self):
        return self.pdiscape.getImage()

    def getSourceImage(self):
        return self.pdispace.getImage().source

    def getLastFileName(self):
        return self.menubar.lastfilename

    def getLastPath(self):
        return self.menubar.lastpath

    def getButtonPressed(self):
        return self.toolbar.indexbselected

    def setSourceImage(self, filename):
        self.pdispace.setSourceImage(filename)


class PdiApp(App):
    """
      Classe principal da aplicação
    """
    def build(self):
        return Pdi()

if __name__=="__main__":
    PdiApp().run()