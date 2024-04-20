from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    completed = SelectField('Completed', choices=[('Yes', 'Yes'), ('No', 'No')])
    validators = [DataRequired()]
    submit = SubmitField('Add Task')