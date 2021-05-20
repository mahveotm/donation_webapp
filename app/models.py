from . import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    street_address = db.Column(db.Text)
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    country = db.Column(db.String(64))
    postal_code = db.Column(db.String(64))
    phone_number = db.Column(db.Integer, nullable=True)
    email_address = db.Column(db.String(64))
    form_of_contact = db.Column(db.String(64))
    form_of_payment = db.Column(db.String(64))
    donation_frequency = db.Column(db.String(64))
    donation_amount = db.Column(db.Integer)
    comment = db.Column(db.Text, nullable=True)
