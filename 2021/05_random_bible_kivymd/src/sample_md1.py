from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen


class Main(MDApp):
    def build(self):
        screen = MDScreen()
        btn = MDRectangleFlatButton(text="Hello World", pos_hint={"center_x": 0.5, "center_y": 0.5})
        screen.add_widget(btn)
        return screen


Main().run()
