import psycopg
from database.query import *
from database.config import Config
import logging 

class PGConn:
	""" PostgreSQL functions """
	def __init__(self):
		self.params = Config.db_config
		try:
			self.conn = psycopg.connect(**self.params)
			self.cur = self.conn.cursor()
		except Exception as e:
			logging.error(e)
			print("Database not configured properly.")
			quit()

	def create(self, fname, lname, username, password):
		try:
			self.cur.execute(create_user(fname, lname, username, password))
			return True
		except (Exception, psycopg.DatabaseError) as error:
			print("[INSERT]",error)
			return False
		
	def delete(self, uid):
		try:
			self.cur.execute(check_uid(uid))
			if self.cur.fetchone():
				self.cur.execute(delete_user(uid))
				return True
			else:
				return False
		except (Exception, psycopg.DatabaseError) as error:
			print("[DELETE]",error)
			return False
		
	def update(self, uid, fname, lname, username, password):
		try :
			self.cur.execute(check_uid(uid))
			if self.cur.fetchone():
				update_data = update_user(uid, fname, lname, username, password)
				if update_data:
					for update in update_data:
						self.cur.execute(update)
					return True
				return False
				
			else:
				return False
		except (Exception, psycopg.DatabaseError) as error:
			print("[UPDATE]",error)
			return False

	def login(self, username):
		try:
			self.cur.execute(login_user(username))
			return  self.cur.fetchone()
		except (Exception, psycopg.DatabaseError) as error:
			print("[LOGIN]",error)
			return 

	def commit(self):
		self.conn.commit()

	def close(self):
		self.cur.close()

	def list_all(self):
		try:
			self.cur.execute(list_all_user())
			all_user = self.cur.fetchall()
			return all_user
		except (Exception, psycopg.DatabaseError) as error:
			print("[LIST ALL]",error)
