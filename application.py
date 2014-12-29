# -*- encoding: utf-8 -*-

from example import AppBuilder


application = app = AppBuilder().build(config='settings.py')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
