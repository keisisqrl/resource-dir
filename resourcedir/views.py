from resourcedir import app, db, Provider
from flask import render_template, url_for, redirect

@app.route('/providers')
@app.route('/')
def list_providers():
    providers = Provider.query.all()
    return render_template("list_providers.html",providers=providers)

@app.route('/provider/')
@app.route('/provider/<id>')
def show_provider(id=None):
    if(id==None):
        return redirect(url_for('list_providers'))
    provider = Provider.query.filter_by(id=id).first()
    return render_template("show_provider.html",provider=provider)

