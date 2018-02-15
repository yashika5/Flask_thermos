from flask import url_for
from flask.ext.testing import TestCase

import thermos
from thermos.models import User, Bookmark

class ThermosTestCase(TestCase):

	def create_app(self):
		return thermos.create_app('test')

	def setUp(self):
		self.db = thermos.db
		self.db.create_all()
		self.client = self.app.test_client()

		u = User(username='sush', email='sush@gmail.com', password='test')
		bm = Bookmark(user=u, url="http://www.example.com", description="example", tags="one,two,three")

		self.db.session.add(u)
		self.db.session.add(bm)
		self.db.session.commit()

		self.client.post(url_for('auth.login'), data = dict(username='sush', password='test'))

	def tearDown(self):
		thermos.db.session.remove()
		thermos.db.session.drop_all()

	def test_delete_all_tags(self):
		response = self.client.post(
			url_for('bookmarks.edit_bookmark', bookmark_id=1),
			data = dict(
				url = "http://test.example.com",
				tags = ""),
			follow_redirects = True
		)

		assert response.status_code == 200
		bm = Bookmark.query.first()
		assert not bm._tags
