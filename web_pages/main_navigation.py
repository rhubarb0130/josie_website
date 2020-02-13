"""Copyright (c) 2020 Josephine Peacock all rights reserved"""
import json

from flask import render_template, request, make_response
from flask.views import View

from web_pages.web_forms import LoginForm

from db_models.flask_data import ContactName, ContactInfo, db


route_file = open('routes.json', 'r')
_routes = json.loads(route_file.read())
route_file.close()


class MainIndex(View):
    methods = ['GET']

    def dispatch_request(self):

        if request.method == 'GET':
            resp = make_response(render_template('Main_Index.html',
                                   cv_download=_routes['josie_cv'],
                                   resume_download=_routes['josie_resume'],
                                   success_stories=_routes['success_stories'],
                                   atta_connect=_routes['atta_connect'],
                                   servo_valve=_routes['servo_valve'],
                                   modular_control=_routes['modular_control'],
                                   web_development=_routes['web_development'],
                                   contact=_routes['contact'],
                                   linkedin=_routes['linkedin'],
                                   github=_routes['github'],
                                   vsi=_routes['vsi'],
                                   yt_valve_test=_routes['yt_valve_test']
                                   ))

            resp.set_cookie("Set-Cookie", "HttpOnly;Secure;SameSite=Strict")  # remove Chrome cross site warning

            return resp


class SucessStories(View):
    methods = ['GET']

    def dispatch_request(self):

        if request.method == 'GET':
            return render_template('Success_Stories.html')


class AttaConnect(View):
    methods = ['GET']

    def dispatch_request(self):

        if request.method == 'GET':
            return render_template('atta_connect.html', main='/')


class ServoValve(View):
    methods = ['GET']

    def dispatch_request(self):
        if request.method == 'GET':
            return render_template('servo_valve.html', main='/')


class ModularControl(View):
    methods = ['GET']

    def dispatch_request(self):
        if request.method == 'GET':
            return render_template('modular_control.html', main='/')


class WebDevelop(View):
    methods = ['GET']

    def dispatch_request(self):
        if request.method == 'GET':
            return render_template('web_development.html', main='/')


class ContactForm(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        form = LoginForm()

        # basically the post but we validate if it's good
        if form.validate_on_submit():
            try:
                if not ContactName.query.filter(ContactName.email == form.email.data).first():
                    add_name = ContactName(first_name=form.firstname.data,
                                           last_name=form.lastname.data,
                                           email=form.email.data
                                           )

                    db.session.add(add_name)
                    db.session.commit()

                    # Only fill out info if something is in the message then find the user id based on the email
                    if form.message.data != '':
                        contact_num = ContactName.query.filter(ContactName.email == form.email.data).first()
                        add_info = ContactInfo(cust_id=contact_num.id,
                                               message=form.message.data)
                        db.session.add(add_info)
                        db.session.commit()

                    db.session.flush()

                else:
                    return 'Got that email already'

            except Exception as e:
                return 'fail'

            return 'success'

        return render_template('contact.html', form=form, main='/')

