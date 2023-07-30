#The code is written by NUHAD N KhanN With his team members
import os
import hashlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.label import Label
from kivy.uix.popup import Popup

MALWARE_SIGNATURES = {
    # Dictionary of known malware signatures
    # Example: 'signature': 'malware_name'
    'd41d8cd98f00b204e9800998ecf8427e': 'MalwareA',
    '098f6bcd4621d373cade4e832627b4f6': 'MalwareB',
    '5eb63bbbe01eeed093cb22bb8f5acdc3': 'MalwareC'
}

class AntivirusApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=(20, 20, 20, 20))
        
        file_button = Button(text='Scan File', size_hint=(None, None), size=(150, 50))
        file_button.bind(on_release=self.scan_file)
        layout.add_widget(file_button)

        directory_button = Button(text='Scan Directory', size_hint=(None, None), size=(150, 50))
        directory_button.bind(on_release=self.scan_directory)
        layout.add_widget(directory_button)

        back_button = Button(text='Back', size_hint=(None, None), size=(150, 50))
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)

        self.result_label = Label(halign='center')
        layout.add_widget(self.result_label)

        self.file_chooser = FileChooserListView()
        layout.add_widget(self.file_chooser)
        
        return layout

    def go_back(self, *args):
        self.file_chooser.path = os.path.dirname(self.file_chooser.path)

    def scan_file(self, *args):
        file_path = self.file_chooser.selection and self.file_chooser.selection[0]
        if file_path:
            malware_name = self._scan_file(file_path)
            if malware_name:
                self._show_popup('Scan Result', f'File is infected with {malware_name}.')
            else:
                self._show_popup('Scan Result', 'File is clean.')
        else:
            self._show_popup('Error', 'Please select a file.')
    
    def scan_directory(self, *args):
        directory_path = self.file_chooser.path
        if directory_path:
            infected_files = self._scan_directory(directory_path)
            if infected_files:
                message = 'Infected files found:\n'
                for file_path, malware_name in infected_files:
                    message += f'{file_path} ({malware_name})\n'
                self._show_popup('Scan Result', message)
            else:
                self._show_popup('Scan Result', 'No infected files found.')
        else:
            self._show_popup('Error', 'Please select a directory.')
    
    def _scan_file(self, file_path):
        with open(file_path, 'rb') as file:
            content = file.read()
            file_hash = hashlib.md5(content).hexdigest()
            if file_hash in MALWARE_SIGNATURES:
                return MALWARE_SIGNATURES[file_hash]
        return None
    
    def _scan_directory(self, directory_path):
        infected_files = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                malware_name = self._scan_file(file_path)
                if malware_name:
                    infected_files.append((file_path, malware_name))
        return infected_files
    
    def _show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    AntivirusApp().run()

