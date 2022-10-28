from django import forms

from expense_tracker_app.expense_tracker.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['budget', 'first_name', 'last_name', 'profile_image']
