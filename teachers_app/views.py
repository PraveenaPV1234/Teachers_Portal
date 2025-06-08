from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, Subjects_Mark
from .forms  import StudentForm, SubjectsMarkForm
from django.contrib import messages
from django.core.paginator import Paginator
from django import forms
class AddStudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    marks = forms.IntegerField(min_value=0, max_value=100)
def get_grade(mark):
    if mark >= 90:
        return 'A+'
    elif mark >= 80:
        return 'A'
    elif mark >= 70:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 50:
        return 'D'
    else:
        return 'F'
def teacher_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def home(request):
    students = Student.objects.all().order_by('name')
    paginator = Paginator(students, 10)  # 10 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    subjects = Subjects_Mark.objects.filter(student__in=page_obj.object_list).select_related('student')

    for subject_mark in subjects:
        subject_mark.grade = get_grade(subject_mark.mark)

    return render(request, 'home.html', {
        'page_obj': page_obj,
        'subjects': subjects 
    })
@login_required
def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            marks = form.cleaned_data['marks'] 
            student,_= Student.objects.get_or_create(name=name)

            subject_obj, created = Subjects_Mark.objects.get_or_create(
                student=student,
                subject=subject,
                defaults={'mark': marks}  
            )

            if not created:
                subject_obj.mark += marks  
                subject_obj.save()

            return redirect('home')
        else:
            messages.error(request, "Invalid input.")
            return redirect('home')

    # Optionally handle GET requests
    return redirect('home')

@login_required
def delete_subject(request, subject_id):
    subject = get_object_or_404(Subjects_Mark, id=subject_id)
    subject.delete()
    return redirect('home')
@login_required
def edit_subject(request, subject_id):
    subject = get_object_or_404(Subjects_Mark, id=subject_id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_subject = request.POST.get('subject')
        new_mark = request.POST.get('marks')  
        if new_name:
            subject.student.name = new_name
            subject.student.save()
        if new_subject:
            subject.subject = new_subject
        if new_mark:
            try:
                subject.mark = int(new_mark)
            except ValueError:
                messages.error(request, "Invalid mark entered.")
                return redirect('home')
        subject.save()
        return redirect('home')
    return render(request, 'home.html', {'subject': subject})
@login_required
def logout_teacher(request):
    logout(request)
    return redirect('login')