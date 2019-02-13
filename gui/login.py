from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from database import User



class RegistrationContent(BoxLayout):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    check_password = ObjectProperty(None)
    email = ObjectProperty(None)

    def checkPass(self):
        self.ids["error_label"].opacity = "1"
        if self.password.text == self.check_password.text:
            self.ids["error_label"].opacity = "0"
            self.ids["send_button"].opacity = "1"

    def register(self):
        u = User(name=self.username.text, surname="ahoj", email=self.email.text, password=self.password.text)
        u.save()



class RegistrationPopup(Popup):
    pass


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.popup = RegistrationPopup()

    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def goNext(self):
        if self.username.text == "ahoj" and self.password.text == "ahoj":
            self.manager.current = "chat_screen"
            self.logged_user = "ahoj"

    def openPopup(self):
        self.popup.open()
