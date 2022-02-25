import bcrypt
from cerberus import Validator
from utils.input_validation_helper import create_user_validation

create_val = Validator(create_user_validation)

hash_salt = bcrypt.gensalt(8)

def set_id():
	uid = input("User ID: ").strip().upper()
	return uid

def set_name():
	first_name = input("First Name: ").strip().upper()
	last_name = input("Last Name: ").strip().upper()
	return first_name, last_name

def set_username():
	username = input("Username: ").strip().lower().replace(' ','')
	return username

def set_password(hashed=False):
	pwinput = input("Password: ").strip()
	if hashed and pwinput!='':
		return bcrypt.hashpw(pwinput.encode(), hash_salt).decode()
	else:
		return pwinput


class Interaction:
	def login_user_data(self):
		username = set_username()
		password = set_password().encode()
		return username, password

	def create_user_data(self):
		fname, lname = set_name()
		username = set_username()
		password = set_password(hashed=True)
		if (fname.replace(' ','').isalpha() and lname.replace(' ','').isalpha() and username.isalpha()):
			val_bool = create_val.validate({'fname':fname,'lname':lname,'username':username,'password':password})
			if val_bool:
				return fname,lname,username,password
			else:
				print(create_val.errors)
		else:
			print("\nEnter valid data\n")

	def del_user_data(self):
		uid = set_id()
		return uid

	def update_user_data(self):
		uid = set_id()
		if uid!='':
			fname, lname = set_name()
			username = set_username()
			password = set_password(hashed=True)
			return uid,fname,lname,username,password

