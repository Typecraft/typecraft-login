from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User
from django import forms


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = UserCreationForm
    fieldsets = UserAdmin.fieldsets #+ (
        #(None, {'fields': ('extra_field1', 'extra_field2',)}),
    #)

admin.site.register(User, MyUserAdmin)
