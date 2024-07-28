from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import Moron

class UserForm(FlaskForm):
    name = StringField("Name of user", validators=[DataRequired()])
    submit = SubmitField("Submit")

class MoronForm(FlaskForm):
    name = StringField("Moron Name", validators=[DataRequired()])
    email = StringField("Moron e-mail", validators=[DataRequired()])
    moron_level = StringField("Moron level")
    submit = SubmitField("Submit")

