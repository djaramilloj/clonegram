from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from posts.models import Post

# Register your models here.
 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'user')
    list_display_links = ('title', 'user')
    # list_editable = ('phone_number', 'website')
    search_fields = ('title', 'user__username')
    list_filter = ('created','modified')

    fieldsets = (
        ('Post Data', {
            "fields": (
              ('user', 'profile',), ('title', 'photo'),
            ),
        }),
        ('Metadata', {
            "fields": (
              ('created', 'modified',),
            ),
        }),
    )

    readonly_fields = (
        'created', 'modified',
    )