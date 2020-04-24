from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import UserProfile

# Register your models here.

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'phone_number', 'website')
    list_display_links = ('user_id','user')
    list_editable = ('phone_number', 'website')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number')
    list_filter = ('created','modified')

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'profile_pic'),       
            ),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('bio')
            )
        }),

        ('Metadata', {
            'fields': (
                ('created', 'modified'),
                
            )
        }),
        
    )

    readonly_fields = ('created', 'modified', 'user')


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'last_name',
        'first_name',
        'is_active',
        'is_staff'

    )

 

admin.site.unregister(User)
admin.site.register(User, UserAdmin)