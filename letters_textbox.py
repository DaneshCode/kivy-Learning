from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class Hani(App):
    def build(self):
        root = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.textbox = TextInput(font_size=30, size_hint=(1, 0.3))
        root.add_widget(self.textbox)

        grid = GridLayout(rows=2, cols=3, spacing=10)
        letters = ["h", "i", "e", "l", "m", "o"]

        for letter in letters:
            btn = Button(text=letter, font_size=30)
            btn.letter = letter
            btn.bind(on_press=self.add_letter)
            grid.add_widget(btn)

        root.add_widget(grid)
        return root

    def add_letter(self, instance):
        self.textbox.text += instance.letter


Hani().run()
