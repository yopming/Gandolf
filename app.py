# -*- coding:utf-8 -*-
from flask import Flask
from utils import decode_markdown

def create_app():
    app = Flask(__name__)
    app.config.update(
        DEBUG=True,
        FILES_ROOT='D:\\webroot\\e\\website\\demos\\ins\\设计稿',
        #FILES_ROOT='.',
        CDN_ROOT='http://demo.vemic.com/demos/ins/设计稿/'
        )

    # jinja trim for blank or next line
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    # make python function available for jinja
    app.jinja_env.globals.update(decode_markdown=decode_markdown)

    return app
