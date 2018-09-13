
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.togglebutton import ToggleButton

class ToolBar(BoxLayout):
    ui = ObjectProperty(None)
    transbutton = ObjectProperty(None)
    bitbutton = ObjectProperty(None)
    histbutton = ObjectProperty(None)
    filterbutton = ObjectProperty(None)
    detbutton = ObjectProperty(None)
    fatbutton = ObjectProperty(None)

    indexbselected = int()

class ButtonTool(ToggleButton):
    toolbar = ObjectProperty(None)

    def set_index(self):
        if self.state == 'down':
            index = self.get_index(self)
            self.toolbar.ui.processingbar.addProperties(index)
            self.toolbar.indexbselected = index

    def get_index(self, widget):
        if self.toolbar.transbutton == widget:
            return 1
        elif self.toolbar.bitbutton == widget:
            return 2
        elif self.toolbar.histbutton == widget:
            return 3
        elif self.toolbar.filterbutton == widget:
            return 4
        elif self.toolbar.detbutton == widget:
            return 5
        elif self.toolbar.fatbutton == widget:
            return 6