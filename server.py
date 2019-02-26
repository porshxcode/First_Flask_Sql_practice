from flask import Flask, render_template, request, redirect
# session, flash
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
# app.secret_key= "secreto"
@app.route("/")
def index():
    mysql = connectToMySQL('first_flask_db')	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/create_friend", methods=["POST"])
def process():
    # is_valid = True		# assume True
    # if len(request.form['fname']) < 1:
    # 	is_valid = False
    # 	flash("*Please enter a first name")
    # if len(request.form['lname']) < 1:
    # 	is_valid = False
    # 	flash("*Please enter a last name")
    # if len(request.form['occ']) < 2:
    # 	is_valid = False
    # 	flash("*Please enter an occupation")
    
    if is_valid:
        query = "INSERT INTO friends (first_name,last_name,occupation,created_at,updated_at) VALUES ( %(fn)s ,%(ln)s,%(oc)s, NOW(),NOW());"
        data = {
            'fn': request.form ['fname'],
            'ln': request.form ['lname'],
            'oc': request.form ['occ']
        }
        db = connectToMySQL('first_flask_db')
        db.query_db(query,data)
        flash("User added succesfully!")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
