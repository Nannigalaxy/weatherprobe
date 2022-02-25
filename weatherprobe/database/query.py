import psycopg
from database.config import Config

user_table = Config.tables['users']

def create_user(first_name, last_name, username, password):
	return str("INSERT INTO {} VALUES ({}, '{}', '{}', '{}', '{}')".format(
		user_table, 'default', first_name, last_name, username, password))

def delete_user(uid):
	try:
		return "DELETE FROM {} WHERE uid = '{}'".format(user_table, uid)
	except (Exception, psycopg.DatabaseError) as error:
			print(error)

def update_user(uid, first_name, last_name, username, password):
	update_data = []
	if uid!='':
		if first_name!='':
			change_fn = "UPDATE {} SET first_name = '{}' WHERE uid = '{}'; ".format(user_table, first_name, uid)
			update_data.append(change_fn)

		if last_name!='':
			change_ln = "UPDATE {} SET last_name = '{}' WHERE uid = '{}'; ".format(user_table, last_name, uid)
			update_data.append(change_ln)

		if username!='':
			change_un = "UPDATE {} SET username = '{}' WHERE uid = '{}'; ".format(user_table, username, uid)
			update_data.append(change_un)

		if password!='':
			change_pw = "UPDATE {} SET password = '{}' WHERE uid = '{}'; ".format(user_table, password, uid)
			update_data.append(change_pw)

	return update_data

def check_uid(uid):
	return "SELECT uid FROM {} WHERE uid = '{}';".format(user_table, uid)

def login_user(username):
	return "SELECT uid, password FROM {} WHERE username = '{}';".format(user_table, username)

def list_all_user():
	return "SELECT uid, first_name, last_name, username FROM {}".format(user_table)