from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import kivy.lang.builder

class CustomDropDown(DropDown):
    pass

class TestApp(App):
    """
      Classe principal da aplicação
    """
    def build(self):
        dropdown = CustomDropDown()
        mainbutton = Button(text='Hello', size_hint=(None, None))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        b = BoxLayout()
        b.add_widget(dropdown)
        return b

if __name__=="__main__":
    TestApp().run()

