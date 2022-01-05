from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, DateField, SelectField
from wtforms.validators import DataRequired, InputRequired
from datetime import datetime

# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember_me = BooleanField('Remember Me')
#     submit = SubmitField('Sign In')


class TemperatureForm(FlaskForm):
    levels = ['Kein', 'Wenig', 'Mittel', 'Stark']

    date = DateField('Datum', [InputRequired(), DataRequired()])
    # date = DateField('Datum', [DataRequired()], '%d.%m.%Y' )
    temperature = FloatField('Temperatur', [DataRequired()])
    first_day = BooleanField('Erster Tag der Periode')
    blood_level = SelectField('Blutintensität', choices=levels, default=0)
    juice_level = SelectField('Schleimqualität', choices=levels, default=0)
    submit = SubmitField('Speichern')
