from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_login, name='login'),
    path('home/', views.home, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('edit_subject/<int:subject_id>/', views.edit_subject, name='edit_subject'),
    path('delete/<int:subject_id>/', views.delete_subject, name='delete_subject'),
    path('logout/', views.logout_teacher, name='logout'),
]