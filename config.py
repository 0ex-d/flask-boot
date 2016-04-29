import os

"""
Config stuffs here
"""
class Config(object):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgres://localhost/sql')
