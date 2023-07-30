#The code is written by NUHAD N KhanN With his team members
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import re
import requests

class PhishingDetector(App):
    def build(self):
        Window.size = (400, 200)
        Window.title = "Phishing Link Detector"
        Window.clearcolor = (0, 0, 1, 1)  # Set default background color to blue
        layout = BoxLayout(orientation='vertical', padding=10)
        self.result_label = Label(text='', font_size=20)
        self.url_input = TextInput(hint_text='Enter URL', multiline=False)
        detect_button = Button(text='Detect', size_hint=(1, 0.5))
        detect_button.bind(on_press=self.detect_phishing)

        layout.add_widget(self.result_label)
        layout.add_widget(self.url_input)
        layout.add_widget(detect_button)

        return layout

    def detect_phishing(self, instance):
        url = self.url_input.text
        if self.is_phishing(url):
            self.show_popup("Phishing Link Detected!")
            self.result_label.text = "Phishing Link Detected!"
            self.update_gui_color((1, 0, 0, 1))  # Set background color to red
        else:
            self.show_popup("Safe Link")
            self.result_label.text = "Safe Link"
            self.update_gui_color((0, 1, 0, 1))  # Set background color to green


    def is_phishing(self, url):
        # Add your phishing detection logic here
        # You can check for indicators such as suspicious domains, mismatched URLs, etc.
        # Example:
        pattern = re.compile(r'^https://', re.IGNORECASE)
        return not bool(pattern.match(url))

    def show_popup(self, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10)
        popup_layout.add_widget(Label(text=message))

        go_back_button = Button(text='Go Back', size_hint=(1, 0.5))
        go_back_button.bind(on_press=self.dismiss_popup)
        popup_layout.add_widget(go_back_button)

        popup = Popup(title='Phishing Link Detected',
                      content=popup_layout,
                      size_hint=(None, None),
                      size=(400, 200))
        popup.open()

    def dismiss_popup(self, instance):
        # Clear the URL input and dismiss the popup
        self.url_input.text = ""
        instance.parent.parent.parent.parent.dismiss()
        self.update_gui_color((0, 0, 1, 1))  # Reset background color to blue

    def update_gui_color(self, color):
        # Update the GUI background color
        Window.clearcolor = color

if __name__ == '__main__':
    PhishingDetector().run()
