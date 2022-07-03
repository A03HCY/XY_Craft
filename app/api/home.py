from flask          import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login    import current_user, login_user, logout_user, login_required
from app.extensions import db
from app.models     import *

home_blue = Blueprint('home', __name__, url_prefix='/')

