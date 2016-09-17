from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import Required



app = Flask(__name__)

class NameForm(Form):
    name = SelectMultipleField("Occupation", "Location")
    #submit = SubmitField('Submit')


#connect a webpage, make name in quotes also function definition below it
#tying a url to a python function
#returning from a function is basically the servers reponse
#never put html directly into return text

#drop down menu
@app.route('/', methods=['GET','POST'])
def drop_down():
    error=""
    if request.method == 'POST':   
        occ = (request.form.get['occ'])
        loc = (request.form.get['loc'])
        if occ is not None and loc is not None:       
            workout = Workout(occ=occ, loc=loc)
            db.session.add(workout)
            db.session.commit() 

            # you can redirect to home page on successful commit. or anywhere else
            return redirect(url_for('index'))       
        else:
            error = "Error, your log is incomplete! Please check and submit it again!"

    return render_template("index.html", error=error)


#make sure we only run the app when this file is called directly
if __name__ == "__main__":
	app.run(debug=True)



