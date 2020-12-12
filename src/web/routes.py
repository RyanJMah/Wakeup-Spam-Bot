import flask
import flask_login
import handlers
from werkzeug.security import generate_password_hash, check_password_hash

app_routes = flask.Blueprint("app_routes", __name__, template_folder = "templates")

def is_logged_in():
	return flask_login.current_user.is_authenticated

@app_routes.route("/")
def index():
	if is_logged_in():
		return flask.redirect(flask.url_for("app_routes.alarm_clock"))
	else:
		return flask.redirect(flask.url_for("app_routes.login"))


@app_routes.route("/alarm-clock", methods = ["GET", "POST"])
def alarm_clock():
	if flask.request.method == "POST":
		pass
		print(flask.request.form)

	if is_logged_in():
		return flask.render_template("clock.html")
	else:
		return flask.redirect(flask.url_for("app_routes.login"))


@app_routes.route("/login", methods = ["GET", "POST"])
def login():
	if flask.request.method == "POST":
		user = handlers.login_handler(
			flask.request.form["username"],
			flask.request.form["password"]
		)
		if user:
			flask_login.login_user(user)
			print("here")
			return flask.redirect(flask.url_for("app_routes.alarm_clock"))
		else:
			flask.flash("Invalid credentials.")

	return flask.render_template("login.html")

