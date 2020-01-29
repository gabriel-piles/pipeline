import logging
import os

import graypy
from flask import Flask

graylog = logging.getLogger('graylog')
graylog.setLevel(logging.INFO)

handler = graypy.GELFUDPHandler(os.environ['GRAYLOG_IP'], 12201, localname="crawler_server")
graylog.addHandler(handler)

app = Flask(__name__)

graylog.info('Pipeline test server running')


@app.route('/')
def info():
    graylog.info('Pipeline test server called')
    return os.getenv('GRAYLOG_IP', 'no variable gotten')
