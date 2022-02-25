from database.postgres import PGConn
import unittest

pgconn = PGConn()

class TestPostgres(unittest.TestCase):

	def test_create(self):
		self.assertEqual(pgconn.create('fname','lname','username','password'), True)

	def test_update(self):
		self.assertEqual(pgconn.update('uid', 'fname', 'lname', 'username', 'password'), False)

	def test_remove(self):
		self.assertEqual(pgconn.delete('uid'), False)

