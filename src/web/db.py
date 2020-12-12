import os
import flask_login
import user
import mysql.connector as sql

def write_db(username, password):
	hashed_passwd = generate_password_hash(password, method = "sha256")
	print(hashed_passwd)

def query_db_id(id_in):
	db = sql.connect(
		host = str(os.environ.get("MARIADB_HOST")).replace("\r", ""),
		user = str(os.environ.get("MARIADB_USER")).replace("\r", ""),
		password = str(os.environ.get("MARIADB_PASSWORD")).replace("\r", ""),
		database = str(os.environ.get("MARIADB_DATABASE")).replace("\r", "")
	)
	cursor = db.cursor()

	query = f"SELECT * FROM users WHERE id = {id_in};"
	cursor.execute(query)
	result = cursor.fetchone()
	db.close()
	return result

def query_db_username(username):
	db = sql.connect(
		host = str(os.environ.get("MARIADB_HOST")).replace("\r", ""),
		user = str(os.environ.get("MARIADB_USER")).replace("\r", ""),
		password = str(os.environ.get("MARIADB_PASSWORD")).replace("\r", ""),
		database = str(os.environ.get("MARIADB_DATABASE")).replace("\r", "")
	)
	cursor = db.cursor()

	query = f"SELECT * FROM users WHERE username = '{username}';"
	cursor.execute(query)
	result = cursor.fetchone()
	db.close()
	return result


def main():
	from werkzeug.security import generate_password_hash, check_password_hash

	query_results = query_db_id(1)
	print(query_results)
	if query_results:
		# print(check_password_hash(query_results[-1], "I hate you2!"))
		print(query_results)
	else:
		print("asdfasdf")

if __name__ == "__main__":
	main()
