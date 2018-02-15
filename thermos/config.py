import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = '\xf7g\xd7`\x08f\xc1\xeer\x00)\xa0#r\xad\x07\xb0\xc9:\xc6\xccZ\xa1>'
	DEBUG = False
	DEBUG_TB_INTERCEPT_REDIRECTS = False

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'thermos.db')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
	WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'thermos.db')

config_by_name = dict(
	dev = DevelopmentConfig,
	test = TestingConfig,
	prod = ProductionConfig
)


