from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, validators
from werkzeug.datastructures import MultiDict

class OpenForm(FlaskForm):
   question = StringField(validators=[validators.DataRequired(message='Please enter the answer')])

   def reset(self):
      blankData = MultiDict([ ('csrf', self.generate_csrf_token() ) ])
      self.process(blankData)

class QuizForm(FlaskForm):
   question = RadioField(validators=[validators.DataRequired(message='Please choose the answer')])