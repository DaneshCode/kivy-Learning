from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Calculator(App):
    def on_btn_press(self, instance):
        txt = instance.text

        if txt == "Clear":
            self.input.text = ""
        elif txt == "save":
            self.save = self.input.text
        elif txt == "show save":
            self.input.text = self.save
        elif txt == "=":
            self.input.text = str(eval(self.input.text))
        else:
            self.input.text += txt

    def build(self):
        self.save = ""
        root = BoxLayout(orientation="vertical", spacing=8, padding=16)

        self.input = TextInput(font_size=32)
        root.add_widget(self.input)

        buttons = [
            ["*", "1", "2", "3"],
            ["/", "4", "5", "6"],
            ["-", "7", "8", "9"],
            ["+", "=", "0", "Clear"],
            ["save", "show save"],
        ]

        for row in buttons:
            grid = GridLayout(cols=len(row), spacing=5)
            for key in row:
                btn = Button(text=key)
                btn.bind(on_press=self.on_btn_press)
                grid.add_widget(btn)
            root.add_widget(grid)

        return root


Calculator().run()
