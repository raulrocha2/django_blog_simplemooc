from django.contrib import admin

from .models import Course

# Customizar Course /admin Django
class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'start_date', 'create_at']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug':('name', 'start_date')}

admin.site.register(Course, CourseAdmin)
