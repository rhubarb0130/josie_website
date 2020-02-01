"""Copyright (c) 2020 Josephine Peacock all rights reserved"""
import json

from flask import Flask

from web_pages.main_navigation import MainIndex
from web_pages.download_content import CvDownload

route_file = open('routes.json', 'r')
_routes = json.loads(route_file.read())
route_file.close()

app = Flask(__name__)

# Index
app.add_url_rule(_routes['main_index'], view_func=MainIndex.as_view('main_index'))
app.add_url_rule(_routes['josie_cv'], view_func=CvDownload.as_view('cv_download'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)