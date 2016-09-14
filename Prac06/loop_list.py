from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class loopListApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        # Construct main app
        super().__init__(**kwargs)
        self.names = ["Jack", "Jenny", "Peter", "Pauline", "Chris", "Ryan"]

    def build(self):
        # Build Kivy GUI
        self.title = "Loop Through Names"
        self.root = Builder.load_file('loop_list.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            self.root.ids.entriesBox.add_widget(Label(text='[color=ff69b4]{}'.format(name), markup=True))


loopListApp().run()