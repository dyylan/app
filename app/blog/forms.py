from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length
from ..models import BlogPost

class BlogPostForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired(), Length(1, 64)])
    title = StringField('Title', validators=[DataRequired(), Length(1, 150), ])
    description = StringField('Description', validators=[DataRequired(), Length(1, 350)])
    file = FileField('Blog post', validators=[FileRequired(), FileAllowed(['md'], 'Markdown files only!')])
    submit = SubmitField('Upload file')

    def validate_title(self, field):
        if BlogPost.query.filter_by(title=field.data).first():
            raise ValidationError('Title has already been used.')