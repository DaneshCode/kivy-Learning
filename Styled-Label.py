from kivy.app import App
from kivy.uix.label import Label

class B(App):
    def build(self):
        return Label(text='Styled Label \n Line two \n Line three \n [b]Bold[/b] and [color=ff3333]new color[/color] ' , halign='center',valign='middle', markup=True, font_size='24sp' , color=(0.1,0.26,0.52),text_size=(300,None))

B().run()
