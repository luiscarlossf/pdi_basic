import platform

from cv2 import imwrite, imread
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from filechooser import LoadDialog, SaveDialog


class MenuBar(BoxLayout):
    ui = ObjectProperty(None)
    openbutton = ObjectProperty(None)
    savebutton = ObjectProperty(None)
    lastfilename = list()
    lastpath = str()

    def show_load(self):
        print(self.ui)
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.lastfilenames = filename
        self.lastpath = path
        self.ui.pdispace.add_image(filename[0])
        self.dismiss_popup()

    def save(self, path, filename):
        img = imread(self.ui.pdispace.get_image().source)
        if platform.system() == 'Windows':
            filename = path + '\\' + filename
        else:
            filename = path + '/' + filename
        imwrite(filename, img)
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()
