from flask import Flask, render_template, request
from forms import ContactForm
import serial

app = Flask(__name__)

def connectArduino():
  try:
    return serial.Serial('/dev/ttyACM0', 9600)
  except:
    return False

@app.route('/')
def home():
  if connectArduino():
    return"CONNECTION"
  else:
    return "NOPE"

@app.route('/contact')
def contact():
  return "Contact"
  
if __name__ == '__main__':
  app.run(debug=True)

