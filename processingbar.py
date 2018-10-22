from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from properties import DefaultProperties, TransformProperties, BitProperties, HistogramProperties
from properties import DetectionProperties, FatColorProperties, FilterProperties, NoiseProperties
from properties import MorphProperties



class ProcessingBar(BoxLayout):
    ui = ObjectProperty(None)
    image_currant = str()
    index = -1
    p = [DefaultProperties(), TransformProperties(ui=ui), BitProperties(), HistogramProperties(ui=ui),
         FilterProperties(), DetectionProperties(), FatColorProperties(), NoiseProperties(ui=ui), MorphProperties()]

    def add_properties(self, index):
        self.index = index
        self.clear_widgets()
        self.p[index].ui = self.ui
        self.add_widget(Label(text='Propriedades', size_hint=(1, 0.2)))
        self.add_widget(self.p[index])
        self.add_widget(RevertButton(
            self.ui, self, text='Reverter', size_hint=(1, 0.3)))
        self.add_widget(CloseButton(
            self.ui, text='Fechar Imagem', size_hint=(1, 0.3)))
        try:
            self.set_histogram(self.ui.pdi_space.get_image().source)
        except AttributeError:
            pass

    def set_histogram(self, filename):
        if self.index == 3:
            self.p[self.index].set_histogram(filename)
            self.p[self.index].hist.reload()


class RevertButton(Button):
    def __init__(self, ui, processing_bar, **kwargs):
        self.pb = processing_bar
        self.ui = ui
        super(RevertButton, self).__init__(**kwargs)

    def on_press(self):
        self.ui.pdi_space.set_source_image(self.pb.image_currant)
        self.ui.pdi_space.get_image().reload()
        self.ui.processing_bar.set_histogram(self.pb.image_currant)



class CloseButton(Button):
    def __init__(self, ui,  **kwargs):
        self.ui = ui
        super(CloseButton, self).__init__(**kwargs)

    def on_press(self):
        panel_images = self.ui.pdi_space.panel_images
        panel_images.content.source = " "
        panel_images.remove_widget(panel_images.content)
        panel_images.remove_widget(panel_images.current_tab)
        try:
            panel_images.switch_to(panel_images.tab_list[0], do_scroll=False)
        except IndexError:
            panel_images.clear_widgets()


