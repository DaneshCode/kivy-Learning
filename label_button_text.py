from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window


class M(App):
    def build(self):
        root = Widget()

        wx = Window.width // 2
        wy = Window.height - 120

        label = Label(text="", pos=(wx - 100, wy), size=(200, 50))

        def on_press(instance):
            label.text += instance.text

        letters = ["h", "a", "n", "i"]
        for idx, l in enumerate(letters):
            btn = Button(text=l, size=(100, 100), pos=(wx - 300 + idx * 100, wy - 200))
            btn.bind(on_press=on_press)
            root.add_widget(btn)

        root.add_widget(label)
        return root


M().run()
