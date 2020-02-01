"""Copyright (c) 2020 Josephine Peacock all rights reserved"""
import json

from flask import render_template, request, send_file
from flask.views import View

route_file = open('routes.json', 'r')
_routes = json.loads(route_file.read())
route_file.close()

class MainIndex(View):
    methods = ['GET']

    def dispatch_request(self):

        if request.method == 'GET':
            return render_template('Main_Index.html',
                                   cv_download=_routes['josie_cv'])

