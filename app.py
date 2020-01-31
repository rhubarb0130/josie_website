"""Copyright (c) 2020 Josephine Peacock all rights reserved"""

from flask import Flask

from web_pages.main_navigation import MainIndex

app = Flask(__name__)

# Index
app.add_url_rule('/', view_func=MainIndex.as_view('main_index'))

if __name__ == "__main__":
    app.run(port=5000, debug=True)