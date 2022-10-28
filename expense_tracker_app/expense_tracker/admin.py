from django.contrib import admin

from expense_tracker_app.expense_tracker.models import Profile, Expense


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass