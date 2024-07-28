from flask import Flask, render_template, flash, request
from App import app, db
from forms import UserForm, MoronForm
from models import Moron

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)

@app.route("/moron/add", methods=["GET", "POST"])
def add_moron():
    name = None
    form = MoronForm()
    if form.validate_on_submit():
        user = Moron.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Moron(name = form.name.data, email = form.email.data, moron_level=form.moron_level.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = None
        form.email.data = None
        form.moron_level.data = None
        flash("New Moron has been added successfully")
    our_users = Moron.query.order_by(Moron.date_added)
    return render_template("add_moron.html", form=form, name = name, our_users = our_users)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route("/moron", methods=['GET', 'POST'])
def moron():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Moron added successfully!")
    return render_template("moron.html",
        name = name,
        form = form)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = MoronForm()
    name_to_update = Moron.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        name_to_update.moron_level = request.form['moron_level']
        try:
            db.session.commit()
            flash('Moron Updated Successfully')
            return render_template('update.html', form=form, name_to_update=name_to_update)
        except:
            flash('Moron Update Failed')
            return render_template('update.html', form=form, name_to_update=name_to_update)
    else:
        return render_template('update.html', form=form, name_to_update=name_to_update)

@app.route("/delete/<int:id>")
def delete(id):
    user_to_delete = Moron.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("Moron deleted!")
        name = None
        form = MoronForm()
        our_users = Moron.query.order_by(Moron.date_added)
        return render_template("add_moron.html", form=form, name = name, our_users = our_users)
    except:
        flash("Moron refuses to get deleted, try again!")



