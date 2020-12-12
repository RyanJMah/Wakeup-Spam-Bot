import db

def get_user_from_id(id_in):
	results = db.query_db_id(id_in)
	if results:
		return User(*results)
	else:
		return None

class User():
	def __init__(self, id_init, username_init, passwd_init):
		self.id = id_init
		self.username = username_init
		self.password = passwd_init

		# self.is_authenticated = True
		# self.is_active = True
		# self.is_anonymous = False

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id