from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from simplemooc.courses.models import Course

from model_mommy import mommy

class CourseManageTestCase(TestCase):

	def setUp(self):
		self.courses_test = mommy.make(
			'courses.Course', name='Teste mommy', _quantity=5
			)
		

	def tearDown(self):
		Course.objects.all().delete()

	def test_course_search(self):
		search = Course.objects.search('mommy')
		self.assertEqual(len(search), 5)		