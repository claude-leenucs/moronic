from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate

### URL for Database ###
                    # "mysql+pymysql://root:my-secret-pw@mysql-dock:3306/newusers"
###     End URL      ###

app = Flask(__name__)
dbPass = os.getenv("DB_PASS")
dbContIP = os.getenv("DB_IP")
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:" + dbPass + "@" + dbContIP + ":3306/newusers"  
app.config['SECRET_KEY'] = "my-secret-pw"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
import routes

@app.before_first_request
def setup():
    db.create_all()
    
if __name__ == "__main__":
    app.run(debug=True)




