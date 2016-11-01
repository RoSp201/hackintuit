
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, database as db, lm, oid
from .forms import LoginForm
from .models import User

import sys
sys.path.append('side_projects/hackintuit/Data/')
import csvMaker as cm
jobs = cm.jobs.values()
print jobs


@app.route('/')
@app.route('/index')
#@login_required
def index():
    user = User(nickname='Robert', email='Bob@email.com')
    posts = [
    	{
	    	'author': {'nickname': 'Robert'}, 
	        'body': 'Beautiful day in Berkeley!' 
    	}
    ]
    return render_template('index.html', user=user, posts=posts, title="Home Page", jobs={}, location=[])

@app.before_request
def before_request():
    g.user = current_user

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
	if g.user is not None and g.user.is_authenticated:
	   return redirect(url_for('index'))
	form = LoginForm()
	#if valid login id receieved, redirect back to home page
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
	return render_template('login.html', title='Sign In', form=form,  providers=app.config['OPENID_PROVIDERS'])


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    #register this as a valid
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))