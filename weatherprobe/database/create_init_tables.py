import psycopg
from config import Config


def create_tables():
	""" create tables in the database"""
	commands = (
		"""
			CREATE SEQUENCE user_id_seq;
			SELECT setval('user_id_seq', 10000);
				
		""",
		"""
			CREATE TABLE users
			(
			uid text CHECK (uid ~ '^AP[0-9]+$') DEFAULT 'AP' || nextval('user_id_seq') PRIMARY KEY,
			first_name varchar(255) NOT NULL,
			last_name varchar(255) NOT NULL,
			username varchar(255) NOT NULL UNIQUE,
			password varchar(255) NOT NULL,
			UNIQUE (first_name, last_name)
			);
				
		""")

	conn = None
	try:
		params = Config.db_config
		# connect to the PostgreSQL server
		conn = psycopg.connect(**params)

		cur = conn.cursor()

		for command in commands:
			cur.execute(command)

		cur.close()
		conn.commit()
		print("Created Tables successfully")
	except (Exception, psycopg.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


if __name__ == '__main__':
	create_tables()
