from flask import Flask, render_template, request, redirect, url_for, flash, Response
from flask_sqlalchemy import SQLAlchemy
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import os
from werkzeug.utils import secure_filename



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@flaskdb.clysdtuc3hyb.eu-west-3.rds.amazonaws.com/flaskaws'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key="somethingunique"


db = SQLAlchemy(app)

# Create A Model For Table
class BlogPosts(db.Model):
    __tablename__ = 'blogposts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    description = db.Column(db.String(6000))
    

    
@app.route('/')
def index():
    posts = BlogPosts.query.all()
    return render_template('index.html', posts=posts)

@app.route('/add/', methods = ['POST'])
def insert_post():
    if request.method =="POST":
        post = BlogPosts(id = request.form.get('id'),
                         title = request.form.get('title'),
        description = request.form.get('description'))
        db.session.add(post)
        db.session.commit()
        flash("Etape ajoutée avec succès")
        return redirect(url_for('index'))

@app.route('/update/', methods = ['POST'])
def update():
    if request.method == "POST":
        my_data = BlogPosts.query.get(request.form.get('id'))
        my_data.title = request.form['titre']
        my_data.description = request.form['description']

        db.session.commit()
        flash("Etape est mise a jour")
        return redirect(url_for('index'))

@app.route('/delete/<id>/', methods = ['GET','POST'])   
def delete(id):
    my_data = BlogPosts.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Suppression avec succès")
    return redirect(url_for('index'))


  



if __name__ == "__main__":
    app.run(debug=True)