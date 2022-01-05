from datetime import datetime
from app import app
from app.forms import TemperatureForm
from flask import render_template, flash, redirect, url_for
from app.db_access import add_entry, get_all_entries, delete_entry
from app.plot_entries import get_plot
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    graphJSON = get_plot()
    return render_template('index.html', title='Home', graphJSON=graphJSON)


@app.route('/entry', methods=['GET', 'POST'])
def entry():
    form = TemperatureForm()

    if form.validate_on_submit():
        try:
            entry = add_entry(form)
        except Exception as e:
            flash(f"Fehler: {e}")
            return render_template('entry.html', title='Neuer Eintrag', form=form)

        flash(f"Neuer Eintrag erstellt: {entry}")
        return redirect(url_for('index'))

    nowFull = datetime.now()
    today = datetime(nowFull.year, nowFull.month, nowFull.day)
    form.date.data = today
    form.temperature.data = 36.6
    return render_template('entry.html', title='Neuer Eintrag', form=form)


@app.route('/all_entries', methods=['GET'])
def all_entries():
    return render_template('all_entries.html', title='Alle Einträge', entries=get_all_entries())


@app.route('/delete_entry/<id>', methods=['POST'])
def post_delete_entry(id):
    delete_entry(id)
    return render_template('all_entries.html', title='Alle Einträge', entries=get_all_entries())
