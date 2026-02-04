from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class Myapp(App):
    def build(self):
        btn = Button(text="click")
        btn.bind(on_press=self.ok)
        return btn

    def ok(self, instance):
        pop = Popup(
            title="welcome",
            content=Label(text="well"),
            size_hint=(0.6, 0.4),
            auto_dismiss=True,
        )
        pop.open()


Myapp().run()
