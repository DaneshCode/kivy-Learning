from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class M(App):
    def build(self):
        r, c = 3, 3
        root = GridLayout(rows=r, cols=c)
        for i in range(r):
            for j in range(c):
                root.add_widget(Button(text=str(i * j)))
        return root


M().run()
