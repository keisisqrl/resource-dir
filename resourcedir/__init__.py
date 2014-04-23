from flask import render_template, Flask 
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/tmp.rRzKWCMTFH'
db = SQLAlchemy(app)


class Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.pub_date = datetime.utcnow()




import resourcedir.views
