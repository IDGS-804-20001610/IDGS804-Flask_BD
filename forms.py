
from wtforms import Form, StringField, IntegerField, EmailField, validators

class UserForm(Form):
    id = IntegerField('ID', [validators.number_range(min = 1, max = 20, message = 'ID NO válido')])
    nombre = StringField('NOMBRE', [validators.DataRequired(message = 'Nombre NO válido')])
    apaterno = StringField('APELLIDO PATERNO', [validators.DataRequired(message = 'Apellido Paterno NO válido')])
    email = EmailField('CORREO', [validators.DataRequired(message = 'Correo NO válido'), validators.Email(message = 'Ingresa un correo válido')])
