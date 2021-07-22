from flask import Flask, render_template, url_for
from werkzeug.datastructures import MultiDict

from mockdbhelper import MockDBHelper
from forms import JobDescriptionForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

DB = MockDBHelper()

@app.route('/')
def index():
    jobs = DB.getAllJobs()
    jobs = list(map(
        lambda job : {
            'info': job,
            'form': JobDescriptionForm(formdata=MultiDict(job), disabled=True)
        },
        jobs))
    return render_template('home.html', jobs=jobs, newJobForm=JobDescriptionForm(disabled=False))

@app.route('/edit')
def editJob():
    pass

if __name__ == '__main__':
    app.run(debug=True)