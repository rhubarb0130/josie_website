from db_models.db import *


class ContactName(db.Model):
    __tablename__ = 'contact_name'
    id = db.Column('id', db.Integer(), primary_key=True, autoincrement=True)
    first_name = db.Column('first_name', db.String(64), unique=False)
    last_name = db.Column('last_name', db.String(64), unique=False)
    email = db.Column('email', db.String(128), unique=True)  # we will use the email to determine if they're in the db


class ContactInfo(db.Model):
    __tablename__ = 'contact_info'
    id = db.Column('id', db.Integer(), primary_key=True, autoincrement=True)
    cust_id = db.Column('cust_id', db.Integer(), db.ForeignKey('contact_name.id', ondelete='CASCADE', onupdate='CASCADE'))
    message = db.Column('message', db.String(512), unique=False)
