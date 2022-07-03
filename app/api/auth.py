from flask          import Blueprint, render_template, request, redirect, url_for
from flask_login    import current_user, login_user, logout_user
from app.extensions import db
from app.models     import *
from sqlalchemy     import or_

auth_blue = Blueprint('auth', __name__, url_prefix='/auth')

