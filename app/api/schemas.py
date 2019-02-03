from .. import ma
from ..models import BlogPost

class BlogPostSchema(ma.ModelSchema):
    class Meta:
        model = BlogPost

        