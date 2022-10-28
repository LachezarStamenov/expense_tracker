from django.urls import path

from expense_tracker_app.expense_tracker.views import index, create_expense, edit_expense, delete_expense, show_profile, \
    edit_profile, delete_profile, create_profile

urlpatterns = (
    path('', index, name='index'),
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>/', edit_expense, name='edit expense'),
    path('delete/<int:pk>/', delete_expense, name='delete expense'),
    path('profile/', show_profile, name='show_profile'),
    path('profile/create/', create_profile, name='create_profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

)