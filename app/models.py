from app import db

class CycleEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True)
    temperature = db.Column(db.Float)
    blood_level = db.Column(db.String(64))
    juice_level = db.Column(db.String(64))
    first_day = db.Column(db.Boolean, index=True)

    def __repr__(self):
        return f'Eintrag: {self.date} {self.temperature}°C'

    def to_dict(self):
        return {
            'date' : self.date,
            'temperature' : self.temperature,
        }