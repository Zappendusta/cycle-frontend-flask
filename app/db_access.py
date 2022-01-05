from app import app, db
from app.models import CycleEntry
from datetime import datetime
from app.forms import TemperatureForm
from typing import List

def add_entry(form:TemperatureForm) -> CycleEntry:

    entry = CycleEntry()
    entry.date = form.date.data
    entry.temperature = form.temperature.data
    entry.blood_level = form.blood_level.data
    entry.juice_level = form.juice_level.data
    entry.first_day = form.first_day.data

    dt = datetime(entry.date.year,entry.date.month,entry.date.day)

    entry_today = CycleEntry.query.filter_by(date=dt).first()

    if entry_today is not None:
        raise Exception(f'Es gibt für heute bereits einen Eintrag: {entry_today}')

    db.session.add(entry)
    db.session.commit()

    return entry

def get_all_entries() -> List[CycleEntry]:
    all_entries = CycleEntry.query.all()
    return sorted(all_entries, key=lambda x: x.date, reverse=True)

def delete_entry(id):
    entry = CycleEntry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
