from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Course, Enrollment
from .forms import ContactCourse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
	courses = Course.objects.all()
	template_name = 'courses/index.html'
	context = {
		'courses':courses
	}
	return render(request, template_name, context)

# def details(request, pk):
	
# 	course = get_object_or_404(Course, pk=pk)
# 	context = {
# 		'course': course
# 	}
# 	template_name = 'courses/details.html'
# 	return 	render(request, template_name, context)
#  

def details(request, slug):
	course = get_object_or_404(Course, slug=slug)
	context = {}
	if request.method == 'POST':
		form = ContactCourse(request.POST)
		if form.is_valid():
			context['is_valid'] = True	
			form.send_mail(course)
			form = ContactCourse()
	else:
		form = ContactCourse()

	context['form']= form
	context['course'] = course
	template_name = 'courses/details.html'
	return 	render(request, template_name, context)

@login_required
def enrollment(request, slug):
	course = get_object_or_404(Course, slug=slug)
	enrollment, created = Enrollment.objects.get_or_create(
		user=request.user, course=course
	)
	if created:
		messages.success(request, 'Inscrição concluida com sucesso!')

	else:
		messages.info(request, 'Você já esta inscrito neste curso!')
	return redirect('accounts:dashboard')	


@login_required
def undo_enrollments(request, slug):
	course = get_object_or_404( Course, slug=slug)
	enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
	if request.method == 'POST':
		enrollment.delete()
		messages.success(request, 'Inscricao cancelada com sucesso')
		return redirect('Accounts:dashboard')
	template = 'courses/undo_enrollments.html'
	context = {
		'enrollment':enrollment,
		'course':course
	}
	return render(request, template, context)

@login_required
def announcements(request, slug):
	course = get_object_or_404(Course, slug=slug)
	if not request.user.is_staff:
		enrollment = get_object_or_404(Enrollment,
			user=request.user, course=course
		)
		if not enrollment.is_approved():
			messages.error(request, 'Se inscreva neste curso')
			return redirect('accounts:dashboard')

	template_name = 'courses/announcements.html'
	context = {
		'course': course,
		'announcements': course.announcements.all()
	}		
	return render(request, template_name, context)		