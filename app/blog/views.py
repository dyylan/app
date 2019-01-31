from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from . import blog
from .. import db
from .. import mongo
from ..decorators import admin_required
from ..models import User, BlogPost
from ..emails import send_email
from .forms import BlogPostForm
from datetime import datetime
from markdown2 import markdown

@blog.route('/submit-blog-post', methods=['GET', 'POST'])
@login_required
@admin_required
def submit_blog_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        file_md = form.file.data.read()
        file_html = markdown(file_md)
        post = {
            "author"            : form.author.data,
            "username"          : current_user.username,
            "email"             : current_user.email,
            "last_edited"       : datetime.utcnow(),
            "created"           : datetime.utcnow(),
            "title"             : form.title.data,
            "description"       : form.description.data,     
            "file_md"           : file_md,
            "file_html"         : file_html
        }
        posts = mongo.db["posts"]
        post_id = posts.insert_one(post).inserted_id
        blogpost = BlogPost(mongo_id=str(post_id),
                            title=form.title.data,
                            author=current_user._get_current_object())
        db.session.add(blogpost)
        db.session.commit()
        flash("Blog post successfully uploaded!")
    for field in form.errors:
        for error in form.errors[field]:
            flash(f"{field.capitalize()} - {error}")
    return render_template('blog/submitblogpost.html', form=form)

@blog.route('/posts')
def get_blog_posts():
    first_post = mongo.db.posts.find_one()
    return render_template('blog/posts.html', post=first_post["file_html"])