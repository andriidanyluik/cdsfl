from flask import Flask, render_template, url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///table.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Table_Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    place = db.Column(db.String(300), nullable=False)
    decision = db.Column(db.String(300), nullable=False)
    who_fix = db.Column(db.String(60), nullable=False)
    fix = db.Column(db.String(60), nullable=False)
    operation_personal = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Table_Journal %r>' % self.id


class Table_av_vym(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rem = db.Column(db.String(60), nullable=False)
    odg = db.Column(db.String(60), nullable=False)
    datez = db.Column(db.DateTime, default=datetime.now())
    datepo = db.Column(db.DateTime, default=datetime.now())
    zazem = db.Column(db.String(300), nullable=False)
    pokaz = db.Column(db.String(300), nullable=False)
    name_who = db.Column(db.String(300), nullable=False)
    workrza = db.Column(db.String(300), nullable=False)
    pr = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<Table_av_vym %r>' % self.id


'''
class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
'''

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/av_vym')
def edit_av():
    return render_template("av_vym.html")


@app.route('/journal')
def edit_journal():
    return render_template("journal.html")


@app.route('/addj', methods=['POST', 'GET'])
def new_journal():
    if request.method == "POST":
        #id = request.form['id']
        place = request.form['place']
        decision = request.form['decision']
        who_fix = request.form['who_fix']
        fix = request.form['fix']
        operation_personal = request.form['operation_personal']

        journal = Table_Journal(place=place, decision=decision,
                                who_fix=who_fix, fix=fix, operation_personal=operation_personal)

        try:
            db.session.add(Table_Journal)
            db.session.commit()
            return redirect('/')
        except:
            return "При створенні запису сталась помилка"
    else:
        return render_template("create_journal.html")


@app.route('/adda')
def new_av_vym():
    return render_template("create_av_vym.html")


@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return "User page " + name+ "-" + str(id)


if __name__ == "__main__":
    app.run(debug=True)