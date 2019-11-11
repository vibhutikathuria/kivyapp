import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader,Sound
from kivy.lang import Builder
Builder.load_string('''
<MenuPage>:
    BoxLayout:
        orientation:'vertical'
        Button:
            text:'ALLAHUAKBAR'
            on_press:root.plays()
''')

class MyApp(App):
    def build(self):
        video = Video(source='C:/Users/Vibhuti/Downloads/allahuakbar.mp4')
        video.state='play'
        video.options = {'eos': 'loop'}
        video.allow_stretch=True
        return video

if __name__ == '__main__':
    MyApp().run()