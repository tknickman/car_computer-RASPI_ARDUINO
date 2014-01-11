from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators, TextAreaField, RadioField
 
class ContactForm(Form):
  radio = RadioField('led', choices=[('on','On'),('off','Off')])
  submit = SubmitField("Send")

