from django.test import TestCase
from django.core import mail
from django.test.client import Client
from django.urls import reverse
from django.conf import settings
from django.core import mail

from simplemooc.courses.models import Course


class ContactCourseTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Django', slug='tests-django')


    def tearDown(self):
        self.course.delete()

    def test_contact_form_error(self):
        data = {'name': 'Fulano do Teste', 'email':'', 'message':''}
        client = Client()
        path = reverse('Courses:details', args=[self.course.slug])
        response = client.post(path, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')

    def test_contact_form_success(self):
        data = {'name': 'Fulano do Teste', 'email':'admin@django.com', 'message':'Teste e-mail success!'}
        client = Client()
        path = reverse('Courses:details', args=[self.course.slug])
        response = client.post(path, data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [settings.CONTACT_EMAIL])  