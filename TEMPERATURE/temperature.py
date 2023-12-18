from flask import Flask, render_template, request

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

@app.route('/')
def index():
    return render_template('index.html', result="")

@app.route('/convert', methods=['POST'])
def convert():
    try:
        celsius = float(request.form['celsius'])
        fahrenheit = float(request.form['fahrenheit'])
        if celsius:
            result = celsius_to_fahrenheit(celsius)
        elif fahrenheit:
            result = fahrenheit_to_celsius(fahrenheit)
        else:
            result = ""
    except ValueError:
        result = "Invalid input. Please enter a valid number."
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
