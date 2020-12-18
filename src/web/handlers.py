import os
import sys
import json
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import db
import user
THIS_DIR = os.path.abspath(os.path.dirname(__file__))
ALARM_DIR = os.path.join(os.path.dirname(THIS_DIR), "alarm")
sys.path.append(ALARM_DIR)
import alarm


def login_handler(username_in, password_in):
	query_results = db.query_db_username(username_in)
	if query_results:		
		if check_password_hash(query_results[-1], password_in):
			return user.User(*query_results)

	return None

def upload_alarm_handler(table_list):
	print(db.query_alarm_db_user("Test1"))

	





def main():
	set_alarm_handler(4, 6, 0, "AM")

if __name__ == "__main__":
	main()	


