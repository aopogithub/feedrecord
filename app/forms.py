from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField,DateTimeField
from wtforms.validators import DataRequired, NumberRange

class FeedingRecordForm(FlaskForm):
    feeding_type = SelectField('喂养方式', choices=[('breast', '亲喂'), ('bottle', '瓶喂')], validators=[DataRequired()])
    amount = IntegerField('喂养量 (毫升)', validators=[DataRequired(), NumberRange(min=1)])
    notes = StringField('备注')
    submit = SubmitField('添加记录')
    class Meta:
        csrf = False

class DeleteRecordForm(FlaskForm):
    submit = SubmitField('确认删除')
    class Meta:
        csrf = False