try:
     from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
    'description': 'TADA',
    'author': 'FANT4STIC',
    'url':'',
    'download_url': ' ',
    'author_email': 'asfdasf@afjdl.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages':['Name'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)
