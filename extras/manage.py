#! /usr/bin/env python

import os

from thermos import create_app, db

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('THERMOS_ENV') or 'dev')
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

#@manager.command
#def initdb():
#	db.create_all()
#	db.session.add(User(username="yashika", email="yashika9n@gmail.com", password="yashika"))
#	db.session.add(User(username="rekha", email="yashika@amagi.com", password="rekha"))
#	db.session.commit()
#	print 'Initialized the database'

@manager.command
def insert_data():
	yashika = User.query.get_or_404(1)
	#yashika = User(username="yashika", email="yashika9n@gmail.com", password="yashika")
	#db.session.add(yashika)

	#rekha = User(username="rekha", email="yashika@amagi.com", password="rekha")
	#db.session.add(rekha)

	def add_bookmark(url,description,tags):
		db.session.add(Bookmark(url=url, description=description, user=yashika, tags=tags))

	#for name in ["python","flask","programming","training","news","data","entertainment","mails"]:
	#	db.session.add(Tag(name=name))

	

	add_bookmark("https://www.google.co.in/","Google main page","news,training,entertainment")
	add_bookmark("https://app.pluralsight.com/player?course=ruby-fundamentals&author=alex-korban&name=ruby-fundamentals-module3&clip=5&mode=live","Ruby pluralsight","programming,training")
	add_bookmark("https://www.codecademy.com/learn","Codeacademy main pag","training,entertainment")
	add_bookmark("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin","Gmail main page","mails,entertainment")
	add_bookmark("https://www.hackerrank.com/","Hackerrank main page","programming")

	db.session.commit()
	print 'Initialized the database'

@manager.command
def dropdb():
	if prompt_bool(
	"Are you sure you want to lose all your data"):
		db.drop_all()
		print 'Dropped the database'

if __name__ == '__main__':
	manager.run()