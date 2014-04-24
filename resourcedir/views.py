from resourcedir import app, db, models, forms
from flask import render_template, url_for, redirect, request
from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form


@app.route('/')
@app.route('/providers')
def list_providers():
    providers = models.Provider.query.all()
    return render_template("list_providers.html",providers=providers)

@app.route('/provider/')
@app.route('/provider/<id>')
def show_provider(id=None):
    if(id==None):
        return redirect(url_for('list_providers'))
    provider = models.Provider.query.filter_by(id=id).first()
    return render_template("show_provider.html",provider=provider)

@app.route('/provider/<id>/delete')
def delete_provider(id):
    db.session.delete(models.Provider.query.filter_by(id=id).first())
    db.session.commit()
    return redirect(url_for('list_providers'))

@app.route('/provider/create', methods=('GET', 'POST'))
def create_provider():
    form = forms.ProviderForm()
    if request.method == 'POST' and form.validate_on_submit():
	provider = models.Provider(form.name.data,form.description.data)
	db.session.add(provider)
	db.session.commit()
	return redirect(url_for('show_provider',id=provider.id))
    return render_template('create_provider.html',form=form)
    
