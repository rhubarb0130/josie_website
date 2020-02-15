"""Copyright (c) 2020 Josephine Peacock all rights reserved"""
from flask import Flask

import json

from web_pages.main_navigation import MainIndex, AttaConnect, ServoValve, ModularControl, WebDevelop, SucessStories,\
    ContactForm
from web_pages.download_content import CvDownload, ResumeDownload

from db_models.flask_data import *

route_file = open('routes.json', 'r')
_routes = json.loads(route_file.read())
route_file.close()

secret_file = open('secret.json', 'r')
_secret = json.loads(secret_file.read())
secret_file.close()

app = Flask(__name__)


class ConfigClass(object):
    SQLALCHEMY_DATABASE_URI = _secret['sql_connection_string']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = _secret['app_secret_key']
    RECAPTCHA_PUBLIC_KEY = _secret['recaptcha_public']
    RECAPTCHA_PRIVATE_KEY = _secret['recaptcha_private']


app.config.from_object(__name__ + '.ConfigClass')

app.config['TESTING'] = True  # Set this to True so recaptcha doesn't annoy us

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


# Main Navigation
app.add_url_rule(_routes['main_index'], view_func=MainIndex.as_view('main_index'))
app.add_url_rule(_routes['atta_connect'], view_func=AttaConnect.as_view('atta_connect'))
app.add_url_rule(_routes['servo_valve'], view_func=ServoValve.as_view('servo_valve'))
app.add_url_rule(_routes['modular_control'], view_func=ModularControl.as_view('modular_control'))
app.add_url_rule(_routes['web_development'], view_func=WebDevelop.as_view('web_development'))
app.add_url_rule(_routes['contact'], view_func=ContactForm.as_view('contact_form'))
app.add_url_rule(_routes['success_stories'], view_func=SucessStories.as_view('success_stories'))

# downloads
app.add_url_rule(_routes['josie_cv'], view_func=CvDownload.as_view('cv_download'))
app.add_url_rule(_routes['josie_resume'], view_func=ResumeDownload.as_view('resume_download'))


if __name__ == "__main__":

    app.run(port=5000, debug=True)