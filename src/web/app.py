import os
import flask
import flask_login
import datetime
import functools
import user
from routes import app_routes

TIMEOUT_MINUTES = 2

def app_init(app):
	app.secret_key = str(os.environ["APP_SECRET_KEY"]).replace("\r", "").encode()
	app.register_blueprint(app_routes)
	@app.before_request
	def make_session_permanent():
		flask.session.permanent = True
		app.permanent_session_lifetime = datetime.timedelta(minutes = TIMEOUT_MINUTES)

	login_manager = flask_login.LoginManager()
	login_manager.init_app(app)
	@login_manager.user_loader
	def load_user(user_id):
		return user.get_user_from_id(user_id)

def main():
	app = flask.Flask(__name__)
	app_init(app)
	app.run(debug = True, host = "0.0.0.0")


if __name__ == "__main__":
	main()

