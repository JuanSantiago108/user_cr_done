from flask import Flask, render_template, request, redirect

from user import User
app = Flask(__name__)
@app.route("/")
@app.route("/users")
def home():
    
    users = User.get_all()
    print(users)
    return render_template("read_page.html", users=users)


from user import User
@app.route('/user/new')
def get_all_user():
    return render_template("create_page.html")





@app.route('/user/new', methods=['POST'])
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