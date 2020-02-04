"""Copyright (c) 2020 Josephine Peacock all rights reserved"""
import json

from flask import Flask

from web_pages.main_navigation import *
from web_pages.download_content import *

route_file = open('routes.json', 'r')
_routes = json.loads(route_file.read())
route_file.close()

app = Flask(__name__)

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
    app.run(host='0.0.0.0', port=5000, debug=True)