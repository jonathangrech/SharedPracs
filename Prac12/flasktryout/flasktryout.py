from flask import Flask

app = Flask(__name__)


def celsius_to_fahrenheit(temp_in_celsius):
    fahrenheit = float(temp_in_celsius) * 9.0 / 5 + 32
    return "{:.2f} F".format(fahrenheit)

@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)

@app.route('/show_converted_temp')
@app.route('/show_converted_temp/<temp_in_celsius>')
def show_converted_temp(temp_in_celsius=0):
    input_details = "Input temperature: {} C".format(temp_in_celsius)
    output_details = "Converted to fahrenheit: {}".format(celsius_to_fahrenheit(temp_in_celsius))
    return "{}<br/>{}".format(input_details, output_details)


if __name__ == '__main__':
    app.run()
