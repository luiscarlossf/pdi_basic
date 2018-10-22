from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.slider import Slider
from kivy.uix.image import Image
import numpy as np
from scipy import ndimage
#Builder.load_file('es.kv')


Builder.load_string('''
<SelectableImage>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size

<RV>:
    id:_rv_slices
    viewclass: 'SelectableImage'
    scroll_type: ['bars', 'content']
    scroll_wheel_distance: dp(114)
    bar_width: dp(10)
    SelectableRecycleBoxLayout:
        orientation: 'horizontal'
        default_size: dp(90), None
        default_size_hint: None, 1
        size_hint_x: None
        width: self.minimum_width - 90
        spacing: dp(2)
        multiselect: False
        touch_multiselect: False

''')

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableImage(RecycleDataViewBehavior, Image):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    rv = None

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableImage, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableImage, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        self.rv = rv
        if is_selected:
            self.rv.type_es = index
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.type_es = 0
        self.data = [{'source': './es_images/es1.png'},\
        {'source': './es_images/es2.png'},\
        {'source': './es_images/es3.png'},\
        {'source': './es_images/es4.png'},\
        {'source': './es_images/es5.png'},\
        {'source': './es_images/es6.png'},\
        {'source': './es_images/es7.png'}]
        #self.data = [{'text': str(x)} for x in range(100)]


"""
class ES(BoxLayout):
    min_l = ObjectProperty(None)
    max_l = ObjectProperty(None)
    min_c = ObjectProperty(None)
    max_c = ObjectProperty(None)
    tam_text = ObjectProperty(None)
    es_label = ObjectProperty(None)

    def get(self):
        print(int(self.max_c.value))
        if self.tam_text.text == "":
            a = ""
        else:
            a = np.zeros((int(self.tam_text.text),int(self.tam_text.text)), dtype=np.int)
            a[int(self.min_l.value):int(self.max_l.value), int(self.min_c.value):int(self.max_c.value)] = 1
            print("Get: ", a)
        return str(a)

    def update(self):
        self.min_l.max = self.min_c.max = int(self.tam_text.text)
        self.max_l.max = self.max_c.max = int(self.tam_text.text)
        self.es_label.text = self.get()

class SliderES(Slider):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            #print(self.get())
            pass
        return super(SliderES, self).on_touch_down(touch)
    
    def get(self):
        pass
"""
class TestApp(App):
    def build(self):
        return RV()

if __name__ == '__main__':
    TestApp().run()