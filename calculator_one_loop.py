from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Key(App):
    def build(self):
        root = GridLayout(rows=2)

        self.textbox = TextInput(text="")
        root.add_widget(self.textbox)

        layout = GridLayout(cols=4)

        labels = [
            "save",
            "1",
            "2",
            "3",
            "-",
            "/",
            "4",
            "5",
            "6",
            "+",
            "7",
            "8",
            "9",
            "*",
            "0",
            "=",
            "clear",
        ]

        for i in labels:
            btn = Button(text=i)
            btn.bind(on_press=self.ok)
            layout.add_widget(btn)

        root.add_widget(layout)
        self.saved = ""
        return root

    def ok(self, instance):
        self.textbox.text += instance.text


Key().run()
