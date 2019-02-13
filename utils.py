import os
from kivy.lang.builder import Builder


def load_kivy():
    for file in os.scandir(os.path.join(os.getcwd(), "kivy_files")):
        Builder.load_file(file.path)

