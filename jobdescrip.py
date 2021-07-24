from flask import Flask, render_template, request, url_for, redirect
from werkzeug.datastructures import MultiDict

from mockdbhelper import MockDBHelper
from forms import JobDescriptionForm, JobDescriptionAddForm
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
            'form': JobDescriptionForm(formdata=MultiDict(job))
        },
        jobs))
    return render_template('home.html', jobs=jobs, newJobForm=JobDescriptionAddForm())

@app.route('/edit')
def editJob():
    pass

@app.route('/add', methods=['POST'])
def addJob():
    EXCLUDED_KEYS = ['csrf_token', 'submit']
    job_info = request.form.to_dict(flat=True)
    for key in EXCLUDED_KEYS:
        if key in job_info:
            del job_info[key]

    DB.addJob(job_info)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)