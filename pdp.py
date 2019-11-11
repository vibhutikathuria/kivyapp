import kivy

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader,Sound
from kivy.lang import Builder
Builder.load_string('''
<MenuPage>:
    BoxLayout:
        orientation:'vertical'
        Button:
            text:'Skrattar du forlorar du'
            on_press:root.plays()

        Image:
            source: 'C://Users//Vibhuti//Downloads//pdp.jfif'
            size_hint: None, None
            size: 400, 400
''')

class MenuPage(Screen):
    M = SoundLoader.load('C://Users//Vibhuti//Downloads//skrattar.mp3')
    def plays(self):
        if MenuPage.M.state == 'stop':
            MenuPage.M.play()
        else:
            MenuPage.M.stop()


sm = ScreenManager()
menu = MenuPage(name='menu')
sm.add_widget(menu)


class pewdiepie(App):
    def build(self):
        return sm

pewdiepie().run()