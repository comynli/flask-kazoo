# coding=utf-8

from setuptools import setup

__author__ = 'comyn'


with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='Flask-ElasticSearch',
    version='0.1',
    download_url='https://github.com/lixm/flask-kazoo/',
    license='BSD',
    author='comyn',
    author_email='li.xm87@gmail.com',
    description='KazooClient for Flask',
    long_description=long_description,
    py_modules=['flask_kazoo'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'kazoo',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)