import os
import toga
import vdf
from steam import determine_steam_directory, parse_vdf, determine_users

class SaveVaultApp:
    def __init__(self):
        self.app = toga.App("SaveVault", "com.cherryyeti.savevault", startup=self.build)
        self.steam_users = []
        self.first_button = toga.Button("Hello world", on_press=self.button_handler)

    def button_handler(self, widget):
        steam_directory = determine_steam_directory()
        if steam_directory:
            print(steam_directory)
            vdf_path = os.path.join(steam_directory, "userdata/1261175423/config/shortcuts.vdf")
            # print(parse_vdf(vdf_path))
            self.steam_users = determine_users(steam_directory)
            self.first_button.text = "Steam Directory Found"  # Update button text
        else:
            print("Steam directory not found.")
            self.first_button.text = "Steam Directory Not Found"  # Update button text

    def test_button(self, widget):
        print(self.steam_users)

    def build(self, app):
        box = toga.Box()

        self.first_button.style.padding = 50
        self.first_button.style.flex = 1
        box.add(self.first_button)

        current_dir = os.path.dirname(__file__)
        icon_path = os.path.join(current_dir, "icons/check.png")
        icon = toga.Icon(icon_path)

        button2 = toga.Button(on_press=self.test_button, icon=icon)
        button2.style.padding = 50
        button2.style.flex = 1
        box.add(button2)

        return box

    def main(self):
        self.app.main_loop()

if __name__ == "__main__":
    SaveVaultApp().main()
