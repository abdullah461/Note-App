#  this is were we create our database models
from . import db
from flask_login import UserMixin #helps us log user in
from sqlalchemy.sql import func

# note model 
class Note(db.model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Interger, db.ForeignKey('user.id'))

# setting up user model
class User(db.Model, UserMixin):
    # schema
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # creating relationships(for references)
    notes = db.relationship('Note')

