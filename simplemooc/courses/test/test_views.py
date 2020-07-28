from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from simplemooc.courses.models import Course


class HomeViewTest(TestCase):
    def test_home_status_code(self):
        client = Client()
        response = client.get(reverse('Core:home'))
        self.assertEqual(response.status_code, 200)

        def test_home_template_used(self):
            client = Client()
            response = client.get(reverse('Core:home'))
            self.assertTemplateUsed(response, 'home.html')
            self.assertTemplateUsed(response, 'base.html')

class TestContactCourseMail(TestCase):
	
	def setUp(self):
		self.course = Course.objects.create(name='Django Test', slug='django-teste')


	def tearDown(self):
		self.course.delete()


	def test_contact_form_error(self):
		data = {'name': 'teste name', 'email': '', 'message': ''}
		client = Client()
		path = reverse('Courses:details', args=[self.course.slug])
		response = client.post(path, data)
		self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
		self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')		