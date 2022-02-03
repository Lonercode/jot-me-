from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy 
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "77666%%%4$3fdt%%5f5"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db=SQLAlchemy(app)

class users(db.Model):
        id = db.Column("id", db.Integer, primary_key=True)
        name = db.Column("name", db.String(100))
        email = db.Column("email", db.String(100))
        password = db.Column("password", db.String(100))

        def __init__(self,name, email, password):
                self.name = name
                self.email = email
                self.password = password 

@app.route('/', methods=["POST", "GET"])
def home():
        if request.method == "POST":
                email = request.form['em1']
                session["email"] = email
                password = request.form['pass2']
                session["password"] = password
                found=users.query.filter_by(email=email, password=password).first()
                if found:
                        return redirect(url_for('user'))
                else:
                        flash("Register first or Log in...", "info")
                        return redirect(url_for('home'))
        else:
                return render_template('home.html')

@app.route('/user')
def user():
        return render_template('user.html')


@app.route('/SignUp', methods=["POST", "GET"])
def SignUp():
        if request.method == "POST":
                name = request.form['nme']
                email = request.form['em']
                password = request.form['pass1']
                usr = users(name,email,password)
                db.session.add(usr)
                db.session.commit()
                return redirect(url_for('home'))
        return render_template('signup.html')



@app.route('/view')
def view():
        return render_template('view.html', values=users.query.all())


@app.route('/delete')
def delete():
        db.session.query(users).delete()
        db.session.commit()
        return redirect(url_for('home'))




@app.route('/logout')
def logout():
        if "email" in session:
                session.pop('email')
        return redirect(url_for('home'))


if __name__=='__main__':
        
        db.create_all()
        app.run(debug=True)