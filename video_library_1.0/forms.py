from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, TextAreaField, validators
from wtforms.validators import DataRequired


class MusicVideoLibraryDraft(FlaskForm):
    title = StringField('Video Title', validators=[DataRequired()])
    band = StringField('Band Name', validators=[DataRequired()])
    genre = StringField('Music Kind', validators=[DataRequired()])