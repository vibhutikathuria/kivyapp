import kivy
from kivy.app import App
from kivy.uix.label import Label

class Myapp(App):
	def build(self):
		return Label(text='Rick Astley for president 2020')


if __name__ == "__main__":
	Myapp().run()