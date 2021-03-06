from django import forms
from django.contrib.auth.forms import UserCreationForm as OldUserCreationForm

from users.models import User


class UserCreationForm(OldUserCreationForm):
    class Meta(OldUserCreationForm.Meta):
        model = User
        fields = ('username', 'email',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
