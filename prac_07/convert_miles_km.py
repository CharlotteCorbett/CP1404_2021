"""Create convert miles to kilometers app"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_CONVERSION = 1.609


class ConvertMilesToKmApp(App):
    message = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        result = self.get_valid_miles() * MILES_CONVERSION
        self.root.ids.output_result.text = str(result)

    def handle_increment(self, value):
        new_input = self.get_valid_miles() + value
        self.root.ids.input_number.text = str(new_input)
        self.handle_calculate()

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKmApp().run()