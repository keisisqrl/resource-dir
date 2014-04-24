from flask import render_template, Flask 
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/tmp.rRzKWCMTFH'
db = SQLAlchemy(app)


import resourcedir.views
