from kivy.app import App
from kivy.uix.button import Button


class Main(App):
    def build(self):
        return Button(text="Hello World", size_hint=(0.5, 0.5))


Main().run()
