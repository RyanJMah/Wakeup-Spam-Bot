import os
import sys
import db
import user
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

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


def set_alarm_handler(hour, minute, second, am_pm):
	def am_pm_to_24h(hour, minute, second, am_pm):
		if am_pm == "PM":
			return {"hour": hour + 12, "minute": minute, "second": second}
		else:
			return {"hour": hour, "minute": minute, "second": second}

	curr = datetime.datetime.now()
	curr = datetime.datetime(curr.year, curr.month, curr.day, curr.hour, curr.minute, curr.second)
	desired = datetime.datetime(
		year = curr.year,
		month = curr.month,
		day = curr.day,
		**am_pm_to_24h(hour, minute, second, am_pm)
	)

	if (datetime.datetime.time(desired) < datetime.datetime.time(curr)):
		desired += datetime.timedelta(days = 1)

	print(desired)
	alarm.alarm_mainloop(desired)


def clear_alarm_handler():
	pass


def main():
	set_alarm_handler(4, 6, 0, "AM")

if __name__ == "__main__":
	main()	


