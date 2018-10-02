
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class StatusBar(BoxLayout):
    ui = ObjectProperty(None)
    labelright = ObjectProperty(None)
    labelleft = ObjectProperty(None)

    def update_status(self):
        self.labelright.text = self.ui.pdispace.filename
