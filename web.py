#!/usr/bin/env python

import os
import simplejson
import logging
from flask import Flask, Response, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/releases')
def releases():
    try:
        staticdir = '%s/static' % os.path.dirname(os.path.abspath(__file__))
        with open('%s/releases.json' % staticdir) as f:
            contents = f.read()
        return Response(response=contents, mimetype='application/json')
    except IOError, e:
        logging.error('Unable to open releases.json: %s' % e)
        return Response('No data (yet?)')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
