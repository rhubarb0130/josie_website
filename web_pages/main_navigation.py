from flask import render_template, request
from flask.views import View

class MainIndex(View):
    methods = ['GET']

    def dispatch_request(self):

        if request.method == 'GET':
            return render_template('Main_Index.html')
