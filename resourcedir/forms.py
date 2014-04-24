from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, validators, widgets
from wtforms.ext.sqlalchemy.orm import model_form
from resourcedir import models

##class CreateProviderForm(Form):
##    name = StringField('name', validators=[DataRequired()])
##    description = TextAreaField('description', validators=[DataRequired()])

ProviderForm = model_form(models.Provider, base_class=Form, field_args = {
        'name': {
        'validators': [validators.DataRequired()]
    },
    'description': {
        'validators': [validators.DataRequired()],
        'widget': widgets.TextArea()
    }
}, exclude = ['comments'])

CommentForm = model_form(models.Comment, base_class=Form, field_args = {
    'submitter': {
        'validators': [validators.DataRequired()]
    },
    'content': {
        'validators': [validators.DataRequired()],
        'widget': widgets.TextArea()
    }
}, exclude = ['provider'])
