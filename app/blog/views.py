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
        created_at = datetime.utcnow()
        post = {
            "author"            : form.author.data,
            "username"          : current_user.username,
            "email"             : current_user.email,
            "last_edited"       : created_at,
            "created"           : created_at,
            "title"             : form.title.data,
            "description"       : form.description.data,     
            "file_md"           : file_md,
            "file_html"         : file_html
        }
        posts = mongo.db["posts"]
        post_id = posts.insert_one(post).inserted_id
        blogpost = BlogPost(mongo_id=str(post_id),
                            title=form.title.data,
                            created=created_at,
                            author=current_user._get_current_object())
        db.session.add(blogpost)
        db.session.commit()
        flash("Blog post successfully uploaded!")
    for field in form.errors:
        for error in form.errors[field]:
            flash(f"{field.capitalize()} - {error}")
    return render_template('blog/submitblogpost.html', form=form)


@blog.route('/posts', methods=['GET'])
def blog_posts():
    blogposts = BlogPost.query.with_entities(BlogPost.title, BlogPost.mongo_id).all()
    return render_template('blog/posts.html', blogposts=blogposts)


@blog.route('/posts/<ObjectId:post_id>', methods=['GET'])
def blog_post(post_id):
    blogpost = mongo.db.posts.find_one_or_404(post_id)
    return render_template('blog/post.html', 
                            post=blogpost["file_html"],
                            title=blogpost["title"],
                            author=blogpost["author"], 
                            created=blogpost["created"])