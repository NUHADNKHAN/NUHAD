import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window
import os
import subprocess

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        label = Label(text='Cyber Safety')
        self.firewall_button = ToggleButton(text='Firewall: Off', group='features', background_color=(0.27, 0.51, 0.71, 1))
        self.phishing_button = ToggleButton(text='Phishing Detector: Off', group='features', background_color=(0.67, 0.31, 0.29, 1))
        self.wifi_button = ToggleButton(text='Public WiFi Protector: Off', group='features', background_color=(0.29, 0.67, 0.49, 1))
        self.antivirus_button = ToggleButton(text='Antivirus: Off', group='features', background_color=(0.67, 0.59, 0.29, 1))
        self.malware_button = ToggleButton(text='Malware Detector: Off', group='features', background_color=(0.29, 0.47, 0.67, 1))
        back_button = Button(text='Back', size_hint=(None, None), size=(80, 40))

        self.firewall_button.bind(on_release=self.toggle_firewall)
        self.phishing_button.bind(on_release=self.toggle_phishing_detector)
        self.wifi_button.bind(on_release=self.toggle_wifi_protector)
        self.antivirus_button.bind(on_release=self.toggle_antivirus)
        self.malware_button.bind(on_release=self.toggle_malware_detector)
        back_button.bind(on_release=self.go_back)

        layout.add_widget(label)
        layout.add_widget(self.firewall_button)
        layout.add_widget(self.phishing_button)
        layout.add_widget(self.wifi_button)
        layout.add_widget(self.antivirus_button)
        layout.add_widget(self.malware_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'

    def toggle_firewall(self, instance):
        if instance.state == 'down':
            instance.text = 'Firewall: On'
            self.execute_file('firewall.py')
        else:
            instance.text = 'Firewall: Off'
            # Stop or terminate the execution of firewall.py if necessary

    def toggle_phishing_detector(self, instance):
        if instance.state == 'down':
            instance.text = 'Phishing Detector: On'
            self.execute_file('phishing.py')
        else:
            instance.text = 'Phishing Detector: Off'
            # Stop or terminate the execution of phishing.py if necessary

    def toggle_antivirus(self, instance):
        if instance.state == 'down':
            instance.text = 'Antivirus: On'
            self.execute_file('antivirus.py')
        else:
            instance.text = 'Antivirus: Off'
            # Stop or terminate the execution of antivirus.py if necessary

    def toggle_malware_detector(self, instance):
        if instance.state == 'down':
            instance.text = 'Malware Detector: On'
            self.execute_file('malware detector.py')
        else:
            instance.text = 'Malware Detector: Off'
            # Stop or terminate the execution of malware_detector.py if necessary

    def toggle_wifi_protector(self, instance):
        if instance.state == 'down':
            instance.text = 'Public WiFi Protector: On'
            self.execute_file('public_wifi_protector.py')
        else:
            instance.text = 'Public WiFi Protector: Off'
            # Stop or terminate any ongoing processes for public_wifi_protector.py

    def execute_file(self, filename):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, filename)
        subprocess.Popen(['python', file_path])


class CyberSafetyApp(App):
    def build(self):
        # Set window size and title
        Window.size = (400, 400)
        Window.title = 'Cyber Safety'

        # Create screen manager and add screens
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))

        return screen_manager


if __name__ == '__main__':
    # Run the Cyber Safety app
    CyberSafetyApp().run()
