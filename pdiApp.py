# File name: pdiApp.py
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder

kivy.require("1.10.0")

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

    def get_image(self):
        return self.pdiscape.get_image()

    def get_source_image(self):
        return self.pdispace.get_image().source

    def get_last_file_name(self):
        return self.menubar.lastfilename

    def get_last_path(self):
        return self.menubar.lastpath

    def get_button_pressed(self):
        return self.toolbar.indexbselected

    def set_source_image(self, filename):
        self.pdispace.set_source_image(filename)


class PdiApp(App):
    """
      Classe principal da aplicação
    """

    def build(self):
        return Pdi()


if __name__ == "__main__":
    PdiApp().run()
