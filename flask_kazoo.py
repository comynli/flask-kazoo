# coding=utf-8

import logging
from kazoo.client import KazooClient
from flask import current_app
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

__author__ = 'comyn'


class Kazoo(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        logger = logging.getLogger('kazoo.client')
        logger.parent = app.logger
        app.config.setdefault('ZOOKEEPER_HOSTS', 'localhost:2181')
        if hasattr(app, "teardown_appcontext"):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'kazoo'):
            ctx.kazoo.stop()
            ctx.kazoo.close()

    def connect(self):
        kz = KazooClient(hosts=current_app.config.get('ZOOKEEPER_HOSTS'))
        kz.start()
        return kz

    def __getattr__(self, item):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'kazoo'):
                ctx.kazoo = self.connect()
            return getattr(ctx.kazoo, item)
