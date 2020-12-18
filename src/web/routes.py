import os
import flask
import flask_login
import handlers
from werkzeug.security import generate_password_hash, check_password_hash


app_routes = flask.Blueprint("app_routes", __name__, template_folder = "templates")

def is_logged_in():
	return flask_login.current_user.is_authenticated

@app_routes.route('/favicon.ico') 
def favicon(): 
    return flask.send_from_directory(
		os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static'),
		'favicon.ico',
		mimetype='image/vnd.microsoft.icon'
	)

@app_routes.route("/")
def index():
	if is_logged_in():
		return flask.redirect(flask.url_for("app_routes.alarm_clock"))
	else:
		return flask.redirect(flask.url_for("app_routes.login"))

@app_routes.route("/dashboard", methods = ["GET", "POST"])
def dashboard():
	if flask.request.method == "POST":
		handlers.upload_alarm_handler(flask.request.json)

	return flask.render_template("dashboard.html")


@app_routes.route("/alarm-clock", methods = ["GET", "POST"])
def alarm_clock():
	if flask.request.method == "POST":
		print(flask.request.form)
		form = flask.request.form
		
		if form["button"] == "set":
			handlers.set_alarm_handler(form["hrs"], form["mins"], form["secs"], form["am_pm"])
		
		# elif form["button"] == "clear":
		# 	handler

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

