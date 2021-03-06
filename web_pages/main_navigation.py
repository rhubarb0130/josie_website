"""Copyright (c) 2020 Josephine Peacock all rights reserved"""
import json

from flask import render_template, request, make_response
from flask.views import View

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
        if request.method == 'GET':
            return render_template('contact.html', main='/')

        if request.method == 'POST':
            pass