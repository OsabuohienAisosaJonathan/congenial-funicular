from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import os

# List of known malware file signatures (just a basic example)
malware_signatures = [
    "virus.exe",
    "malware.dll",
    "trojan.bat",
]

class AntivirusApp(App):
    def build(self):
        self.title = "Simple Antivirus"
        layout = BoxLayout(orientation="vertical")
        self.result_label = Label(text="")
        self.dir_input = TextInput(hint_text="Enter directory path")
        scan_button = Button(text="Scan Directory")
        scan_button.bind(on_release=self.scan_directory)
        layout.add_widget(self.dir_input)
        layout.add_widget(scan_button)
        layout.add_widget(self.result_label)
        return layout

    def scan_directory(self, instance):
        directory_to_scan = self.dir_input.text
        if not os.path.exists(directory_to_scan):
            self.result_label.text = "Directory does not exist."
            return
        malware_found = self.check_directory(directory_to_scan)
        if malware_found:
            self.result_label.text = "Malware found in the directory."
        else:
            self.result_label.text = "No malware found in the directory."

    def check_directory(self, directory_path):
        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if self.check_file(file_path):
                    return True
        return False

    def check_file(self, file_path):
        for signature in malware_signatures:
            if signature in file_path:
                return True
        return False

if __name__ == "__main__":
    AntivirusApp().run()
