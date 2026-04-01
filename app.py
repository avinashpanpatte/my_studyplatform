from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    link = db.Column(db.String(200), nullable=True)

@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/ds')
def ds():
    return render_template('ds.html')

@app.route('/os')
def os():
    return render_template('os.html')

@app.route('/se')
def se():
    return render_template('se.html')

@app.route('/dbms')
def dbms():
    return render_template('dbms.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)