from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton


class ToolBar(BoxLayout):
    ui = ObjectProperty(None)
    trans_button = ObjectProperty(None)
    bit_button = ObjectProperty(None)
    hist_button = ObjectProperty(None)
    filter_button = ObjectProperty(None)
    det_button = ObjectProperty(None)
    fat_button = ObjectProperty(None)

    index_b_selected = int()



class ButtonTool(ToggleButton):
    tool_bar = ObjectProperty(None)

    def set_index(self):
        if self.state == 'down':
            index = self.get_index(self)
            self.toolbar.ui.processing_bar.add_properties(index)
            self.toolbar.index_b_selected = index

    def get_index(self, widget):
        if self.toolbar.trans_button == widget:
            return 1
        elif self.toolbar.bit_button == widget:
            return 2
        elif self.toolbar.hist_button == widget:
            return 3
        elif self.toolbar.filter_button == widget:
            return 4
        elif self.toolbar.det_button == widget:
            return 5
        elif self.toolbar.fat_button == widget:
            return 6
        elif self.toolbar.noise_button == widget:
            return 7
        elif self.toolbar.morph_button == widget:
            return 8
        elif self.toolbar.seg_button == widget:
            return 9
        elif self.toolbar.comp_button == widget:
            return 10
