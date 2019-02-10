from .. import ma
from ..models import User, Post, BlogPost


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        exclude = ('password_hash',)


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post


class BlogPostSchema(ma.ModelSchema):
    class Meta:
        model = BlogPost


user_schema = UserSchema()
users_schema = UserSchema(many=True)

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

blogpost_schema = BlogPostSchema()
blogposts_schema = BlogPostSchema(many=True)
