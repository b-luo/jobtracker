from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, TextAreaField, validators

class JobDescriptionForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'disabled' not in kwargs:
            kwargs['disabled'] = True

        self.company = StringField(label='Company', render_kw={'disabled': kwargs['disabled']})
        self.role = StringField(label='Role', render_kw={'disabled': kwargs['disabled']})
        self.status = StringField(label='Status', render_kw={'disabled': kwargs['disabled']})
        self.dateApplied = DateField(label='Date Applied', render_kw={'disabled': kwargs['disabled']})
        self.dateReplied = DateField(label='Date Heard Back', render_kw={'disabled': kwargs['disabled']})
        self.location = StringField(label='Location', render_kw={'disabled': kwargs['disabled']})
        self.description = TextAreaField(label='Description', render_kw={'disabled': kwargs['disabled']})
        self.submit = SubmitField(label='Submit')

    