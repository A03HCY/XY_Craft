from app.extensions    import db, manager
from flask_login       import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import datetime, time


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True, index=True)
    username = db.Column(db.String(20), nullable=False, index=True, unique=True, comment='user name')
    realname = db.Column(db.String(8), default='', comment='real name')
    classnum = db.Column(db.String(8), default='', comment='class number')
    password = db.Column(db.String(256), comment='user password')

    role = db.Column(db.String(20), default='', comment='role')
    level = db.Column(db.String(20), default='L0', comment='level')
    status = db.Column(db.String(20), default='unverified', comment='status')
    create_time = db.Column(db.DATETIME, default=datetime.datetime.now)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def retime(self):
        return time.time()


@manager.user_loader
def load_user(id):
    return User.query.get(int(id))

