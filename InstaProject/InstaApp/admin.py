from django.contrib import admin
from .models import Post, Comment, Like,Users,PostTag,Tag,Follow

admin.site.register(Users)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostTag)
admin.site.register(Tag)
admin.site.register(Follow)
# Register your models here.
