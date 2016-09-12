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

    def handle_increase(self, value):
        self.root.ids.input_distance.text = str(int(self.root.ids.input_distance.text) + value)

    def handle_decrease(self, value):
        self.root.ids.input_distance.text = str(int(self.root.ids.input_distance.text) + value)

    def handle_convert(self, value):
        self.root.ids.output_label.text = str(round(int(self.root.ids.input_distance.text) * 1.609344, 3))



ConvertDistanceApp().run()
