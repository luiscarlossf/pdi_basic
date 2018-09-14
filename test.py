from image_pdi import Image as PI
import cv2 as cv
from backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.image import Image

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):
    def build(self):
        b = BoxLayout()
        filename = PI(filename="./images/estrada.jpg").media_filter(5)
        #fcka = FigureCanvasKivyAgg(plt)
        b.add_widget(Image(source=filename))
        return b

if __name__=='__main__':
    TestApp().run()

