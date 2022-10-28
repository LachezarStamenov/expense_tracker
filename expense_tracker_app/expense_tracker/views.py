from django.shortcuts import render, redirect

from expense_tracker_app.expense_tracker.forms import CreateProfileForm, CreateExpenseForm, EditExpenseForm, \
    EditProfileForm, DeleteProfileForm, DeleteExpenseForm
from expense_tracker_app.expense_tracker.models import Profile, Expense


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile
    return None


def index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left,
    }

    return render(request, 'home-with-profile.html', context)


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

    if request.method == 'POST':
        form = CreateExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateExpenseForm()
    context = {
        'form': form,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditExpenseForm(instance=expense)
    context = {
        'form': form,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense,
    }

    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = Profile.objects.first()
    total_items = Expense.objects.count()
    budget_left = profile.budget - sum(e.price for e in Expense.objects.all())

    context = {
        'profile': profile,
        'total_items': total_items,
        'budget_left': budget_left,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)



