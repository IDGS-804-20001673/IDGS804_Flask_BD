from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('id', [validators.number_range(min = 1, max = 20, message='Valor no válido')])
    nombre = StringField('nombre', [validators.DataRequired(message='Valor no válido')])
    apaterno = StringField('apaterno', [validators.DataRequired(message='Valor no válido')])
    email = EmailField('correo', [validators.DataRequired(message='Valor no válido'),
                                  validators.Email(message='Ingresa un correo válido')])
    




