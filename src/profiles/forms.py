from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(help_text="Please enter your website.", required=False)
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

    class Meta:
        model = UserProfile
        fields = ['website', 'picture']


# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         exclude = ('user',)