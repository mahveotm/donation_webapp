from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from . import main
from .forms import NameForm, ReviewForm

@main.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        print(form.donation_frequency.data)
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

        return redirect(url_for("main.preview"))
    return render_template("index.html", form=form)


@main.route("/preview", methods=["GET", "POST"])
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


@main.route("/confirm")
def confirm_proccess():
    if session.get("city"):
        return render_template("success.html")
    return redirect("/")


@main.route("/cancel")
def cancel_proccess():
    if session.get("city"):
        return render_template("cancel.html")
    return redirect("/")
