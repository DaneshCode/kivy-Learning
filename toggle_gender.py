from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton


class MyApp(App):
    def build(self):
        layout = BoxLayout(padding=20, spacing=10)

        self.btn_man = ToggleButton(text="male", group="gender")
        self.btn_wom = ToggleButton(text="female", group="gender")

        self.btn_man.bind(on_press=self.ok)
        self.btn_wom.bind(on_press=self.ok)

        layout.add_widget(self.btn_man)
        layout.add_widget(self.btn_wom)

        return layout

    def ok(self, instance):
        if self.btn_man.state == "down":
            print("🙂 male")
        elif self.btn_wom.state == "down":
            print("🙂 female")


MyApp().run()
