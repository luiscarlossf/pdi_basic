from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.image import Image as CoreImage
from kivy.core.image import ImageData

class Test(BoxLayout):
    pass

class TestApp(App):
    def build(self):
        t = Test()
        im = CoreImage("./images/estrada.jpg")
        imd = ImageData()
        t.add_widget(im.image)
        return Test()

if __name__=="__main__":
    TestApp().run()

