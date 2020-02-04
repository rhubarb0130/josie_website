"""Copyright (c) 2020 Josephine Peacock all rights reserved"""

from flask import request, send_file
from flask.views import View


class CvDownload(View):
    methods = ['GET']

    def dispatch_request(self):

        if request.method == 'GET':
            return send_file('static/downloads/Josie CV.pdf')


class ResumeDownload(View):
    methods = ['GET']

    def dispatch_request(self):
        if request.method == 'GET':
            return send_file('static/downloads/JosiesResume.pdf')