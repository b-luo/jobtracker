from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, TextAreaField, validators

class JobDescriptionForm(FlaskForm):
    company = StringField(label='Company', render_kw={'disabled': True})
    role = StringField(label='Role', render_kw={'disabled': True})
    status = StringField(label='Status', render_kw={'disabled': True})
    dateApplied = DateField(label='Date Applied', render_kw={'disabled': True})
    dateReplied = DateField(label='Date Heard Back', render_kw={'disabled': True})
    location = StringField(label='Location', render_kw={'disabled': True})
    description = TextAreaField(label='Description', render_kw={'disabled': True})
    submit = SubmitField(label='Submit')