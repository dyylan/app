from flask import render_template, redirect, request, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from . import api
from .. import db
from ..models import User, Post, BlogPost 
from .schemas import (user_schema, users_schema,
                      post_schema, posts_schema,
                      blogpost_schema, blogposts_schema)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Users API

@api.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    result = users_schema.dump(users).data
    return jsonify(result)


@api.route('/users/username/<username>', methods=['GET'])
def user_from_username(username):
    user = User.query.filter_by(username=username).first()
    if user:
        result = user_schema.dump(user).data
    else:
        result = {"Error" : "No users with this username."}
    return jsonify(result)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Posts API

@api.route('/posts', methods=['GET'])
def posts():
    posts = Post.query.all()
    result = posts_schema.dump(posts).data
    return jsonify(result)

@api.route('/posts/id/<post_id>', methods=['GET'])
def post_from_id(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post:
        result = post_schema.dump(post).data
    else:
        result = {"Error" : "No posts with this id."}
    return jsonify(result)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Blogposts API

@api.route('/blogposts', methods=['GET'])
def blogposts():
    blogposts = BlogPost.query.all()
    result = blogposts_schema.dump(blogposts).data
    return jsonify(result)


@api.route('/blogposts/id/<blogpost_id>', methods=['GET'])
def blogpost_from_id(blogpost_id):
    blogpost = BlogPost.query.filter_by(id=blogpost_id).first()
    if blogpost:
        result = blogpost_schema.dump(blogpost).data
    else:
        result = {"Error" : "No blog posts with this id."}
    return jsonify(result)


@api.route('/blogposts/blogpostlist', methods=['GET'])
def blogpost_titles():
    blogposts = BlogPost.query.with_entities(BlogPost.title, BlogPost.url).all()
    return jsonify(blogposts)