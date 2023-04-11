from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, InputRequired,Length, Email, EqualTo
from flask_ckeditor import CKEditorField



##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class Comment(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

class RegisterForm(FlaskForm):
    name=StringField("Name", validators=[DataRequired()])
    email = StringField('Email', validators=[InputRequired(), Length(max=60)])
    password = PasswordField('New Password', [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField("Submit")



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(max=60)])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField("Submit")

