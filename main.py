from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class lego(MDApp):
    def build(self):
        return MDLabel(text="Sory, there are no lego sets yet(", halign="center")


lego().run()