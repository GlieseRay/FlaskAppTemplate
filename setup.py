#!/usr/bin/env python


import re
import codecs
import os

from setuptools import setup, find_packages


where_am_i = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(where_am_i, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


long_description = read('README.md')

install_requires = [
    'Flask>=0.9',
]

tests_require = [
    'nose',
    'coverage',
    'virtualenv>=1.10',
    'mock',
]

find_excludes = [
    'instance'
    'static',
    'tests',
]

setup(
    name='example',
    version=find_version('example', '__init__.py'),

    description='A Flask Application Template',
    long_description=long_description,
    url='https://github.com/GlieseRay/FlaskAppTemplate',
    license='MIT',

    author='Ray',
    author_email='gliese.q@gmail.com',

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    keywords='flask app template',

    packages=find_packages(exclude=find_excludes),
    install_requires=install_requires,
    include_package_data=True,

    tests_require=tests_require,
    test_suite='tests',

    zip_safe=False
)
