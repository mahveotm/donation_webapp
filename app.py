import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from wtforms import (
    StringField,
    IntegerField,
    SubmitField,
    SelectField,
    TextAreaField,
    FloatField,
)
from wtforms.validators import DataRequired, Email, Optional, NumberRange

from datetime import timedelta

countries = (
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua & Deps",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cape Verde",
    "Central African Rep",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Comoros",
    "Congo",
    "Congo {Democratic Rep}",
    "Costa Rica",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland {Republic}",
    "Israel",
    "Italy",
    "Ivory Coast",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea North",
    "Korea South",
    "Kosovo",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macedonia",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar, {Burma}",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russian Federation",
    "Rwanda",
    "St Kitts & Nevis",
    "St Lucia",
    "Saint Vincent & the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome & Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Swaziland",
    "Sweden",
    "Switzerland",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad & Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
)

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.permanent_session_lifetime = timedelta(minutes=10)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SECRET_KEY"] = "wjeyfg4rfnxjlkldju83oorui9e3n3m kfod-=djeickd"

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
migrate = Migrate(app, db)


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
    further_comment = db.Column(db.Text, nullable=True)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


class ReviewForm(FlaskForm):
    confirmation = SubmitField("Confirm")
    cancel = SubmitField("Cancel")


class NameForm(FlaskForm):
    last_name = StringField("Last name", validators=[DataRequired()])
    first_name = StringField("First name", validators=[DataRequired()])
    street_address = StringField("Street Adress", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    state = StringField("State/Region", validators=[DataRequired()])
    country = SelectField(label="Country", choices=countries)
    postal_code = StringField("Postal Code", validators=[DataRequired()])
    phone_number = IntegerField("Phone number", validators=[Optional()])
    email_address = StringField("Email", validators=[Email()])
    form_of_contact = SelectField(
        label="Preferred form of contact",
        choices=["phone", "email"],
        validators=[DataRequired()],
    )
    form_of_payment = SelectField(
        label="Preferred form of payment", choices=["USD", "Euro", "Bitcoin"]
    )
    donation_frequency = SelectField(
        label="Frequency of donation", choices=["Monthly", "Yearly", "One-time"]
    )
    donation_amount = FloatField(
        "Amount of donation", validators=[NumberRange(min=1.00, max=1000000.00)]
    )
    further_comment = TextAreaField("Comments", validators=[Optional()])
    submit = SubmitField("Review")


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session["last_name"] = form.last_name.data
        session["first_name"] = form.first_name.data
        session["street_address"] = form.state.data
        session["city"] = form.city.data
        session["state"] = form.state.data
        session["country"] = form.state.data
        session["postal_code"] = form.postal_code.data
        session["phone_number"] = form.phone_number.data
        session["email_address"] = form.email_address.data
        session["form_of_contact"] = form.form_of_contact.data
        session["form_of_payment"] = form.form_of_payment.data
        session["donation_frequency"] = form.donation_frequency.data
        session["donation_amount"] = form.donation_amount.data
        session["further_comment"] = form.further_comment.data

        return redirect(url_for("preview"))
    return render_template("index.html", form=form)


@app.route("/preview", methods=["GET", "POST"])
def preview():
    form = ReviewForm()
    if session.get("city"):
        if form.validate_on_submit():
            print("Hello Africa")
            if form.cancel.data:
                return redirect("/cancel")
            user = User(
                last_name=session.get("last_name"),
                first_name=session.get("first_name"),
                street_address=session.get("street_address"),
                city=session.get("city"),
                state=session.get("state"),
                country=session.get("country"),
                postal_code=session.get("postal_code"),
                phone_number=session.get("phone_number"),
                email_address=session.get("email_address"),
                form_of_contact=session.get("form_of_contact"),
                form_of_payment=session.get("form_of_payment"),
                donation_frequency=session.get("donation_frequency"),
                donation_amount=session.get("donation_amount"),
                comment=session.get("further_comment"),
            )
            db.session.add(user)
            db.session.commit()
            return redirect("confirm")
        return render_template(
            "preview.html",
            form=form,
            last_name=session.get("last_name"),
            first_name=session.get("first_name"),
            street_address=session.get("street_address"),
            city=session.get("city"),
            state=session.get("state"),
            country=session.get("country"),
            postal_code=session.get("postal_code"),
            phone_number=session.get("phone_number"),
            email_address=session.get("email_address"),
            contact_form=session.get("form_of_contact"),
            payment_form=session.get("form_of_payment"),
            donation_frequency=session.get("donation_frequency"),
            further_comment=session.get("further_comment"),
        )
    return redirect("/")


@app.route("/confirm")
def confirm_proccess():
    if session.get("city"):
        return render_template("success.html")
    return redirect("/")


@app.route("/cancel")
def cancel_proccess():
    if session.get("city"):
        return render_template("cancel.html")
    return redirect("/")
