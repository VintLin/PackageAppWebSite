from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    input = StringField('Input...', validators=[DataRequired()])
    submit = SubmitField('添加')


class DeleteForm(FlaskForm):
    submit = SubmitField('删除')