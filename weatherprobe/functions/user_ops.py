import database.query
from database.postgres import PGConn
from functions.interactions import *
from utils import TableIt

db = PGConn()
interact = Interaction()

column_list = ["UID","First Name","Last Name","Username"]

def exit_prompt(msg="Quit"):
	""" Exit prompt confirmation """
	exit = input(f"\n{msg}? [y/n]: ").strip().lower()
	if exit=='y':
		print("Exiting program\n")
		quit()

def login_check():
	""" Handle user login at entry """
	print("\nLogin with username and password\n")
	username, password = interact.login_user_data()
	if username == '':
		exit_prompt()
		return False
	status = db.login(username)
	if status is None:
		print("\nLogin failed! Please check username")
		exit_prompt()
		return False

	elif status:
		uid = status[0]
		pwhash = status[1].encode()
		pwcheck = bcrypt.checkpw(password, pwhash)
		if pwcheck:
			print("\nLogin successful")
			return True, uid, username
		else:
			print("\nWrong password")
			return False
			
def create_user():
	""" Handle user creation """
	user_data = interact.create_user_data()
	if user_data:
		fname, lname, username, password = user_data
		status = db.create(fname,lname,username,password)
		if status:
			db.commit()
			print("\nNew user created successfully")
			return True
		else:
			print("\nNew user creation failed")

def remove_user(current_uid):
	""" Handle user removal """
	uid = interact.del_user_data()
	if current_uid == uid:
		print("\nCannot remove current user")
	else:
		if uid!='':
			status = db.delete(uid)
			if status:
				db.commit()
				print("\nUser removed successfully")
				return True
			else:
				print("\nUser removal failed. Check UID.")
		else:
			print("\nProvide UID")

def update_user():
	""" Handle user update """
	update_user = interact.update_user_data()
	if update_user:
		uid,fname,lname,username,password = update_user
		status = db.update(uid,fname,lname,username,password)
		if status:
			db.commit()
			print("\nUser updated successfully")
			return True
		else:
			print("\nNothing to update")
	else:
		print("\nProvide UID to update user")

def list_users():
	""" Print all user in table """
	users = db.list_all()
	if users:
		users.insert(0, column_list)
		TableIt.printTable(users, useFieldNames=True)
	else:
		print("\nNo users found")

def close_db():
	db.close()

def init_user():
	""" initial user creation """
	if not db.list_all():
		print("\nCreate new login user\n")
		create_user()
