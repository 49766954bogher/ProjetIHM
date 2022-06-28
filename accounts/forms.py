from django import forms
from .models import UserCV
from django.contrib.auth import get_user_model
#from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'picture',)
    

class UserCVForm(forms.ModelForm):
    cv = forms.FileField(label='Upload CV', required=False)
    class Meta:
        model = UserCV
        fields = ('cv',)