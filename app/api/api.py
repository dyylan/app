from flask import render_template, redirect, request, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from . import api
from .. import db
from ..models import BlogPost
from .schemas import BlogPostSchema


@api.route('/blog_posts', methods=['GET'])
def blog_posts():
    blogpost_schema = BlogPostSchema()
    blogposts = BlogPost.all()
    result = blogpost_schema.dump(blogposts)
    return jsonify(result.data)
