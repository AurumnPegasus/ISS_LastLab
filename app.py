from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "studentDatabase.db"))
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)


class Library_L(db.Model):
	pages = db.Column(db.Integer, nullable=False)
	book_name = db.Column(db.String(120), primary_key = True)
	author = db.Column(db.String(80), nullable=False)
	genre = db.Column(db.String(120), nullable=False)	

@app.route("/addBook", methods = ["GET", "POST"] )
def get_data():
    if request.form:
        form = request.form
        book_name = form["inputEmail4"]
        author = form["inputAddress"]
        genre = form["inputCity"]
        pages = form["inputZip"]
        s = Library_L(pages = pages, book_name = book_name, author = author, genre = genre)
        db.session.add(s)
        db.session.commit()
        return redirect(url_for('getBook'))
    return render_template('home.html')

@app.route("/getBook", methods = ["GET"])
def getBook():
    books = Library_L.query.all()
    return render_template('output.html', data=books)
	#return render_template('output.html', data = boo

@app.route('/getAll')
def getOneBook():
	book_name = request.args.get('book_name')
	s = Library_L.query.filter_by(name=book_name).first()
	obj = {
			"book_name" : s.book_name,
			"author" : s.author,
			"genre" : s.genre,
            "pages" : s.pages
	}
	return str(obj)

if __name__=="__main__":
    app.run(debug=True)
