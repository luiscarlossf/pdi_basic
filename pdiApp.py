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
    menu_bar = ObjectProperty(None)
    tool_bar = ObjectProperty(None)
    pdi_space = ObjectProperty(None)
    processing_bar = ObjectProperty(None)
    status_bar = ObjectProperty(None)

    def get_image(self):
        return self.pdiscape.get_image()

    def get_source_image(self):
        return self.pdi_space.get_image().source

    def get_last_file_name(self):
        return self.menu_bar.last_file_name

    def get_last_path(self):
        return self.menu_bar.last_path

    def get_button_pressed(self):
        return self.tool_bar.index_b_selected

    def set_source_image(self, filename):
        self.pdi_space.set_source_image(filename)


class PdiApp(App):
    """
      Classe principal da aplicação
    """
    @staticmethod
    def build():
        return Pdi()


if __name__ == "__main__":
    PdiApp().run()
