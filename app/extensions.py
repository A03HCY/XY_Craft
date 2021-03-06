from flask_sqlalchemy import SQLAlchemy
from flask_login      import LoginManager
from flask_ckeditor   import CKEditor


db      = SQLAlchemy()
editor  = CKEditor()
manager = LoginManager()
manager.login_view = '/auth/sign'