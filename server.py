from flask import Flask, render_template, request, redirect
from user_cr import User
app = Flask(__name__)

@app.route("/")
def home():
    users = User.get_all()
    print(users)
    return render_template("home.html", users = users)

@app.route("/add_new")
def add_new():
    return render_template("new.html")

@app.route('/sucess', methods=["POST"])
def sucess():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.create_new(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

