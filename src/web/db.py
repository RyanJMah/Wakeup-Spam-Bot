import os
import flask_login
import user
import mysql.connector as sql

def write_db(username, password):
	hashed_passwd = generate_password_hash(password, method = "sha256")
	print(hashed_passwd)

def __execute_fetch(sql_str, sql_params, fetchall = False):
	db = sql.connect(
		host = str(os.environ.get("MARIADB_HOST")).replace("\r", ""),
		user = str(os.environ.get("MARIADB_USER")).replace("\r", ""),
		password = str(os.environ.get("MARIADB_PASSWORD")).replace("\r", ""),
		database = str(os.environ.get("MARIADB_DATABASE")).replace("\r", "")
	)
	cursor = db.cursor()
	cursor.execute(sql_str, sql_params)
	if (fetchall):
		results = cursor.fetchall()
	else:
		results = cursor.fetchone()

	db.close()
	return results

def __execute_write(sql_str, sql_params):
	db = sql.connect(
		host = str(os.environ.get("MARIADB_HOST")).replace("\r", ""),
		user = str(os.environ.get("MARIADB_USER")).replace("\r", ""),
		password = str(os.environ.get("MARIADB_PASSWORD")).replace("\r", ""),
		database = str(os.environ.get("MARIADB_DATABASE")).replace("\r", "")
	)
	cursor = db.cursor()
	cursor.execute(sql_str, sql_params)

	db.commit()
	db.close()
	return 1
	

def query_db_id(id_in):
	query = "SELECT * FROM users WHERE id = %(id)s"
	params = {"id": id_in}
	return __execute_fetch(query, params, fetchall = False)
	
def query_db_username(username):
	query = "SELECT * FROM users WHERE username = %(username)s"
	params = {"username": username}
	return __execute_fetch(query, params, fetchall = False)


def query_alarm_db_time(time):
	query = "SELECT * FROM alarms WHERE alarm_time = %(time)s;"
	params = {"time": time}
	return __execute_fetch(query, params, fetchall = True)

def query_alarm_db_user(user):
	query = "SELECT * FROM alarms WHERE user = %(user)s;"
	params = {"user": user}
	return __execute_fetch(query, params, fetchall = True)

def write_alarm_db(row_dict, action = "insert"):
	if action == "insert":
		query = """
			INSERT INTO alarms (user, alarm_name, alarm_msg, alarm_time, phone_number, alarm_type, repeat_alarm)
				VALUES (
					%(user)s,
					%(alarm_name)s,
					%(alarm_msg)s,
					%(alarm_time)s,
					%(phone_number)s,
					%(alarm_type)s,
					%(repeat_alarm)s);
		"""
	elif action == "delete":
		query = """
			DELETE FROM alarms WHERE
				user = %(user)s AND
				alarm_name = %(alarm_name)s AND
				alarm_msg = %(alarm_msg)s AND
				alarm_time = %(alarm_time)s AND
				phone_number = %(phone_number)s AND
				alarm_type = %(alarm_type)s AND
				repeat_alarm = %(repeat_alarm)s;
		"""
	else:
		return False

	return __execute_write(query, row_dict)


def main():
	params = {
		"user": "Test1",
		"alarm_name": "test1",
		"alarm_msg": "this is a test message",
		"alarm_time": "6:30",
		"phone_number": "+14038886969",
		"alarm_type": "call",
		"repeat_alarm": '1'
	}
	write_alarm_db(params, action = "insert")

if __name__ == "__main__":
	main()
