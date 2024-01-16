from flask import Flask, render_template, redirect, url_for, request, session

app=Flask(__name__)
app.secret_key="Ayan"

@app.route("/")
@app.route("/home")
def index():
	return render_template("index.html")

def user():
	usr=session.get("user")
	if "user" in session:
		return redirect(url_for("user"))
	else:
		return redirect(url_for("login"))

@app.route("/login", methods=["GET","POST"])
def login():
	if request.method=="POST":
		usr=session["Username"]
		return redirect(url_for("user"))
	elif "user" in session:
		return redirect(url_for("user"))
	else:
		return redirect(url_for("login"))
		
@app.route("/logout")		
def logout():
	session.pop("Username", None)
	return redirect(url_for("login"))

@app.route("/about")
def about():
	return render_template("about.html")

if __name__=="__main__":
	app.run(debug=True)
