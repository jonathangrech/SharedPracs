from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window



class ConvertDistanceApp(App):

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('distance_converter.kv')
        return self.root

    def handle_increment(self, value):
        self.root.ids.input_distance.text = str(int(self.root.ids.input_distance.text) + value)
        self.handle_convert()

    def handle_convert(self):
        try:
            self.root.ids.output_label.text = str(round(int(self.root.ids.input_distance.text) * 1.609344, 3))
        except ValueError:
            self.root.ids.output_label.text = "0.0"



ConvertDistanceApp().run()
