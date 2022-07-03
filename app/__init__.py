from flask          import Flask, render_template
from app.api.space  import space_blue
from app.api.home   import home_blue
from app.api.auth   import auth_blue
from app.extensions import db, manager, editor
from app.models     import *
from datetime       import timedelta
import click


def create_app():
    app = Flask(__name__)
    app.secret_key = '48fj3-2ldjx-c1drl'
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1) 
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
    app.config['PER_PAGE'] = 10
    register_error_handlers(app)
    register_extensions(app)
    register_blueprint(app)
    register_cmd(app)

    return app


def register_error_handlers(app:Flask):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('error/error.html'), 400

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('error/error.html'), 403

    @app.errorhandler(404)
    def not_found(e):
        return render_template('error/error.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template('error/error.html'), 500


def register_cmd(app: Flask):
    @app.cli.command()
    def resetall():
        click.confirm('Reset the database ( all data will be remove ).', abort=True)
        db.drop_all()
        click.echo('Remove done.')
        db.create_all()
        db.session.commit()
        click.echo('Init done.')


def register_blueprint(app:Flask):
    app.register_blueprint(space_blue)
    app.register_blueprint(home_blue)
    app.register_blueprint(auth_blue)


def register_extensions(app:Flask):
    db.init_app(app)
    manager.init_app(app)
    editor.init_app(app)