from resourcedir import app, db, models, forms
from flask import render_template, url_for, redirect, request
from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form

## providers

@app.route('/')
@app.route('/providers')
def list_providers():
    providers = models.Provider.query.all()
    return render_template("list_providers.html",providers=providers)

@app.route('/provider/')
@app.route('/provider/<id>')
def show_provider(id=None):
    if id == None:
        return redirect(url_for('list_providers'))
    provider = models.Provider.query.filter_by(id=id).first()
    if provider == None:
	abort(404)
    comment_form = forms.CommentForm()
    return render_template("show_provider.html",
	provider=provider,form=comment_form)

@app.route('/provider/<id>/delete')
def delete_provider(id):
    db.session.delete(models.Provider.query.filter_by(id=id).first())
    db.session.commit()
    return redirect(url_for('list_providers'))

@app.route('/provider/create', methods=('GET', 'POST'))
def create_provider():
    form = forms.ProviderForm()
    if form.validate_on_submit():
	provider = models.Provider(form.name.data,form.description.data)
	db.session.add(provider)
	db.session.commit()
	return redirect(url_for('show_provider',id=provider.id))
    return render_template('create_provider.html',form=form)
    
@app.route('/provider/<id>/modify', methods=('GET', 'POST'))
def modify_provider(id):
    provider = models.Provider.query.filter_by(id=id).first()
    if provider == None:
	return abort(404)
    form = forms.ProviderForm(obj=provider)
    if form.validate_on_submit():
	form.populate_obj(provider)
	db.session.commit()
	return redirect(url_for('show_provider',id=provider.id))
    return render_template('modify_provider.html',form=form,provider=provider)

@app.route('/provider/<id>/comment', methods=('GET', 'POST'))
def add_comment(id):
    form = forms.CommentForm()
    if form.validate_on_submit():
	comment = models.Comment(form.submitter.data,
	    form.content.data)
	comment.provider_id = id
	db.session.add(comment)
	db.session.commit()
    return redirect(url_for('show_provider',id=id))
