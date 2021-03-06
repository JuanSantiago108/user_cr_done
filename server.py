from flask import Flask, render_template, request, redirect

from user import User
app = Flask(__name__)



@app.route("/")
def index():
    return redirect("/users")



@app.route("/users")
def users():
    users = User.get_all()
    print(users)
    return render_template("users.html", users=users)





from user import User
@app.route('/user/new')
def get_all_user():
    return render_template("new_users.html")





@app.route('/user/create', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)