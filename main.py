# -*- coding: UTF-8 -*-

import bottle
from bottle import route
from google.appengine.ext.webapp.util import run_wsgi_app


app = bottle.app()


@route('/')
def index():
    return 'Hello world!'


def main():
    bottle.debug(True)
    run_wsgi_app(app)


if __name__ == '__main__':
    main()
