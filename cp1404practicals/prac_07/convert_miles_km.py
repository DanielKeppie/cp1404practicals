from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty
MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculate(self, miles):
        km = miles * MILES_TO_KM
        self.root.ids.output_label.text = str(km)

    def handle_increment(self, miles, change):
        value = miles + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate(miles)


ConvertMilesKm().run()
