"""Copyright (c) 2020 Josephine Peacock all rights reserved"""
import json

from flask import render_template, request
from flask.views import View

route_file = open('routes.json', 'r')
_routes = json.loads(route_file.read())
route_file.close()


class MainIndex(View):
    methods = ['GET']

    def dispatch_request(self):

        if request.method == 'GET':
            return render_template('Main_Index.html',
                                   cv_download=_routes['josie_cv'],
                                   success_stories=_routes['success_stories'],
                                   atta_connect=_routes['atta_connect'],
                                   servo_valve=_routes['servo_valve'],
                                   modular_control=_routes['modular_control'],
                                   contact=_routes['contact']
                                   )


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


class ContactForm(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'GET':
            return render_template('contact.html', main='/')

        if request.method == 'POST':
            pass