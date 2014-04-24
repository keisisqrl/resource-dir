from resourcedir import db
from datetime import datetime

class Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.pub_date = datetime.utcnow()

