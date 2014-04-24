from resourcedir import db
from datetime import datetime

class Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    description = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    comments = db.relationship('Comment', backref='provider',
			       lazy='dynamic',cascade="all,delete-orphan")

    def __init__(self, name, description, location):
        self.name = name
        self.location = location
        self.description = description
        self.pub_date = datetime.utcnow()

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submitter = db.Column(db.String)
    content = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'))

    def __init__(self, submitter, content):
        self.submitter = submitter
        self.content = content
        self.pub_date = datetime.utcnow()
