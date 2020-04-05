from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length
#generar Formulario Registro de Usuario
class SignupForm(FlaskForm):
	name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
	password = PasswordField('Password', validators=[DataRequired()])
	email = StringField('email', validators=[DataRequired(), Email()])
	submit = SubmitField('Registrar')
#Generar Formulario Login Usuario
class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Recuerdame')
	submit = SubmitField('Login')