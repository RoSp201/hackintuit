
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Bob'}  # fake user
    title = "title"
    posts = [
    	{
	    	'author': {'nickname': 'John'}, 
	        'body': 'Beautiful day in Portland!' 
    	}
    ]
    return render_template("index.html", user=user, posts=posts, title=title)
