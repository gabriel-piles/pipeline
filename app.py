import logging

import graypy
from flask import Flask

from secrets import GRAYLOG_IP

graylog = logging.getLogger('graylog')
graylog.setLevel(logging.INFO)

handler = graypy.GELFUDPHandler(GRAYLOG_IP, 12201, localname="crawler_server")
graylog.addHandler(handler)

app = Flask(__name__)

graylog.info('Pipeline test server running')


@app.route('/')
def info():
    graylog.info('Pipeline test server called')
    return 'Pipeline test server called'
