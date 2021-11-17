from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin
from authentication.forms import UserForm,CustomUserChangeForm
# Register your models here.



class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form =CustomUserChangeForm
    model = User
    add_fieldsets=(
    ('Personal Detail', {'fields':('username','full_name','email','password','profile_pic','website', 'bio', 'gender', 'phone_number')}),
    ('Permissions', {'fields':('is_staff','is_active')})
    )
    fieldsets=(
    ('Personal Detail', {'fields':('username','full_name','email','profile_pic', 'website', 'bio', 'gender', 'phone_number')}),
    ('Permissions', {'fields':('is_staff','is_active')})
    )

admin.site.register(User, CustomUserAdmin)
