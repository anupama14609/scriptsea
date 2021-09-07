from django.contrib import admin
from .models import Contact,Post, BlogComment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
admin.site.register(BlogComment)