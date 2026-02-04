from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        btn = Button(text="Open Popup")
        btn.bind(on_press=self.show_popup)
        return btn

    def show_popup(self, instance):
        box = BoxLayout(orientation="vertical")
        box.add_widget(Label(text="This is popup"))
        box.add_widget(Button(text="OK", on_press=lambda x: self.popup.dismiss()))

        self.popup = Popup(
            title="Popup", content=box, size_hint=(0.5, 0.5), auto_dismiss=False
        )
        self.popup.open()


MyApp().run()
