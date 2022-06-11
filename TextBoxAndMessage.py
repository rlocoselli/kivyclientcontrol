import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class TestApp(App):
    def build(self):
        layout = BoxLayout(padding=10)
        button = Button(text='Click here to see a message')
        text = CapitalInput()
        def callback(instance, value):
            popup = Popup(title='Test popup', content=Label(text=text.text),
              auto_dismiss=False)
            popup.open()
        button.bind(state=callback)    
        layout.add_widget(button)
        layout.add_widget(text)
        return layout

class CapitalInput(TextInput):
    
    def insert_text(self, substring, from_undo=False):
        s = substring.upper()
        return super().insert_text(s, from_undo=from_undo)

if __name__ == '__main__':
    TestApp().run()