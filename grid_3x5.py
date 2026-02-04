from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Hani(App):
    def build(self):
        root = GridLayout(rows=3, cols=5)
        for i in range(3):
            for j in range(5):
                root.add_widget(Button(text=f"{i},{j}"))
        return root


Hani().run()
