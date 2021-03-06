# -*- encoding: utf-8 -*-

import os
from flask import Flask

from . import default_settings

class AppBuilder(object):
    """ Application Builder
    """

    def build(self, config=None):
        app = Flask(__name__, instance_relative_config=True)

        # config from default settings
        app.config.from_object(default_settings)

        # config from setting file
        if config is not None:
            app.config.from_pyfile(config)

        # config from system environment parameters
        for key, val in os.environ.items():
            if key.startswith('EXAMPLE_APP_'):
                app.config[key] = val

        @app.route('/')
        def hello_world():
            return 'Hello World!'

        return app
