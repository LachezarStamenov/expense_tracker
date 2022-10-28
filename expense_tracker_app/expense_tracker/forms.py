from django import forms

from expense_tracker_app.expense_tracker.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['budget', 'first_name', 'last_name', 'profile_image']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['budget', 'first_name', 'last_name', 'profile_image']


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'