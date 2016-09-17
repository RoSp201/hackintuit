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

jobs = {
        'S2411_C01_004E':'Management income',
        'S2411_C01_005E':'Busineess Finance Operations',
        'S2411_C01_006E':'Computer engineer/science',
        'S2411_C01_007E':'Computer and Math',
        'S2411_C01_008E':'Architectural engineering',
        'S2411_C01_009E':'Life/Social/Physical science',
        'S2411_C01_011E':'Community and Social',
        'S2411_C01_012E':'Legal',
        'S2411_C01_013E':'Education',
        'S2411_C01_014E':'Arts,sports,design',
        'S2411_C01_016E':'Health Diagnosing',
        'S2411_C01_017E':"Health Technical",
        'S2411_C01_019E':'Health Support',
        'S2411_C01_021E':'Fire Fighting',
        'S2411_C01_022E':'Law Enforcement',
        'S2411_C01_023E':'Food Service',
        'S2411_C01_024E':'Building/Grounds Maintenance',
        'S2411_C01_025E':'Personal care and service',
        'S2411_C01_027E':'Sales',
        'S2411_C01_028E':'Office Administrative',
        'S2411_C01_030E':'Farming, fishing, forestry',
        'S2411_C01_031E':'Construcation & Extraction',
        'S2411_C01_032E':'Installation, maintenance, repair',
        'S2411_C01_034E':'Production Occupation',
        'S2411_C01_035E':'Transportation',
        'S2411_C01_036E':'Material Moving'
}
#connect a webpage, make name in quotes also function definition below it
#tying a url to a python function
#returning from a function is basically the servers reponse
#never put html directly into return text

#drop down menu
@app.route('/', methods=['GET','POST'])
def drop_down():
    error=""
    if request.method == 'POST':
        occ = request.form.get('occ', jobs)
        loc = request.form.get('loc')
        if occ is not None and loc is not None:       
            pass
            #TODO call the function with the trained model
            # to get data

            # you can redirect to home page on successful commit. or anywhere else
            return redirect(url_for('index'))       
        else:
            error = "Error, your log is incomplete! Please check and submit it again!"

    return render_template("index.html", error=error, jobs=jobs)


#make sure we only run the app when this file is called directly
if __name__ == "__main__":
	app.run(debug=True)



