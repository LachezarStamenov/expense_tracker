from django.shortcuts import render, redirect

from expense_tracker_app.expense_tracker.forms import CreateProfileForm
from expense_tracker_app.expense_tracker.models import Profile


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile
    return None


def index(request):
    profile = get_profile()
    if not profile:
        return redirect('create_profile')

    return render(request, 'home-with-profile.html')


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def create_expense(request):
    return render(request, 'expense-create.html')


def edit_expense(request, pk):
    return render(request, 'expense-edit.html')


def delete_expense(request, pk):
    return render(request, 'expense-delete.html')


def show_profile(request):
    return render(request, 'profile.html')


def edit_profile(request):
    return render(request, 'profile-edit.html')


def delete_profile(request):
    return render(request, 'profile-delete.html')


