from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Hani(App):
    def build(self):
        root = GridLayout(rows=6, cols=6)

        for i in range(6):
            for j in range(6):
                if (i + j) % 2 == 0:
                    color = (1, 1, 1, 1)
                else:
                    color = (0, 0, 0, 1)

                btn = Button(
                    text=f"{i},{j}", background_normal="", background_color=color
                )
                root.add_widget(btn)

        return root


Hani().run()
