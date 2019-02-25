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
from bson import ObjectId


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
                            author=form.author.data,
                            description=form.description.data,
                            created=created_at,
                            user=current_user._get_current_object())
        db.session.add(blogpost)
        db.session.commit()
        flash("Blog post successfully uploaded!")
    for field in form.errors:
        for error in form.errors[field]:
            flash(f"{field.capitalize()} - {error}")
    return render_template('blog/submitblogpost.html', form=form)


@blog.route('/blogposts', methods=['GET'])
def blog_posts():
    blogposts = BlogPost.query.with_entities(BlogPost.title, BlogPost.url).all()
    return render_template('blog/posts.html', blogposts=blogposts)


@blog.route('/blogposts/<post_url>', methods=['GET'])
def blog_post(post_url):
    blogpost_db = BlogPost.query.filter_by(url=post_url).first()
    mongo_id = blogpost_db.mongo_id
    blogpost_html = mongo.db.posts.find_one_or_404(ObjectId(mongo_id))['file_html']
    return render_template('blog/post.html', 
                            blogpost_html=blogpost_html,
                            blogpost_db=blogpost_db)