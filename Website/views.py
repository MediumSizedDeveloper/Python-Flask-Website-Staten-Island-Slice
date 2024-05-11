from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import login_required, current_user
from Website.models import Cart, Item
# Create blueprint
views = Blueprint("views", __name__)

@views.route("/")
def home():
    items = Item.query.all() #important
    return render_template("home.html", user=current_user, items=items)


@views.route("/<int:item_id>/add_to_cart")
def add_to_cart(item_id):
    return render_template("check.html")


#used to check if routes work
@views.route("/check")
def check():
    return render_template("check.html")