import os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import MDNavigationDrawer
from utils import load_kivy
from database import Chat, Message, User
from kivy.lang.builder import Builder
from kivy.clock import mainthread
from kivy.uix.scrollview import ScrollView

from .login import LoginScreen

class PongGame(Widget):
    display = ObjectProperty


class AddButton(Button):
    pass


class MessagesLayout(BoxLayout):
    orientation = "vertical"


class ChatLayout(BoxLayout):
    orientation = "horizontal"


class ChatScreen(Screen):
    message_layout = ObjectProperty(None)
    chat_layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for chat in Chat.select():
            b = Button(text=str(chat.tatada))
            print(self.message_layout)
            self.message_layout.add_widget(b)


class RegistrationPopup(Popup):
    pass


class Manager(ScreenManager):
    login_screen = ObjectProperty(None)
    chat_screen = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        c, l = ChatScreen(), LoginScreen()
        self.add_widget(l)
        self.add_widget(c)


class ChatApp(App):
    load_kivy()
    def build(self):
        return Manager()

