from django.test import TestCase
from .models import Student, Subjects_Mark
from .views import add_student
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
class StudentSubjectTestCase(TestCase):
    def setUp(self):
        self.student_name = "Alice"
        self.subject = "Math"
        self.client = Client()
        self.user = User.objects.create_user(username="Teacher1", password="T1235")
        self.client.login(username="Teacher1", password="T1235")

    def test_create_new_student_subject(self):
        response = self.client.post(reverse('add_student'), {
            'name': 'John Doe',
            'subject': 'Math',
            'marks': 50
        })
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Subjects_Mark.objects.count(), 1)
        self.assertEqual(Subjects_Mark.objects.first().mark, 50)

    def test_add_marks_to_existing_subject(self):
        student = Student.objects.create(name='Jane')
        Subjects_Mark.objects.create(student=student, subject='Science', mark=30)

        response = self.client.post(reverse('add_student'), {
            'name': 'Jane',
            'subject': 'Science',
            'marks': 20
        })

        updated_subject = Subjects_Mark.objects.get(student=student, subject='Science')
        self.assertEqual(updated_subject.mark, 50)

    def test_invalid_input_should_fail(self):
        response = self.client.post(reverse('add_student'), {
            'name': '',
            'subject': '',
            'marks': 'invalid'
        }, follow=True) 
        self.assertContains(response, "Invalid input")  
        self.assertEqual(Subjects_Mark.objects.count(), 0)
     #  INTEGRATION TEST
    def test_student_list_after_creation(self):
        self.client.post(reverse('add_student'), {
            'name': 'Sam',
            'subject': 'English',
            'marks': 40
        })

        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Sam')
        self.assertContains(response, 'English')
        self.assertContains(response, '40')

    # END-TO-END TEST
    def test_full_user_flow(self):
        self.client.logout()
        response = self.client.get(reverse('login'), follow=True)
        self.assertContains(response, 'login') 