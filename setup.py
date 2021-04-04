from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'demo',
    version          = '1.1.0',
    description      = 'demo',
    long_description = readme,
    author           = 'mario',
    author_email     = 'hanmario@bu.edu',
    url              = 'http://wiki',
    packages         = ['demo'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'demo = demo.__main__:main'
            ]
        }
)
