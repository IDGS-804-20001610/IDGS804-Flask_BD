
from wtforms import Form, StringField, IntegerField, EmailField, validators

class UserForm(Form):
    id = IntegerField('id', [validators.number_range(min = 1, max = 20, message = 'ID NO válido')])
    nombre = StringField('nombre', [validators.DataRequired(message = 'Nombre NO válido')])
    apaterno = StringField('apaterno', [validators.DataRequired(message = 'Apellido Paterno NO válido')])
    email = EmailField('correo', [validators.DataRequired(message = 'Correo NO válido'), validators.Email(message = 'Ingresa un correo válido')])
