from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout



class StatusBar(BoxLayout):
    ui = ObjectProperty(None)
    label_right = ObjectProperty(None)
    label_left = ObjectProperty(None)

    def update_status(self):
        self.label_right.text = self.ui.pdi_space.filename
