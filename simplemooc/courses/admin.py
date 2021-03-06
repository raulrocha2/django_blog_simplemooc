from django.contrib import admin

from .models import Course, Enrollment, Comment, Announcement, Lesson, Material

# Customizar Course /admin Django
class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'start_date', 'create_at']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug':('name', 'start_date')}


class MaterialInlineAdmin(admin.TabularInline):
	model = Material


class LessonAdmin(admin.ModelAdmin):
	list_display = ['name', 'number', 'course', 'release_date']
	search_fields = ['name', 'description']
	list_filter = ['created_at']

	inlines = [
		MaterialInlineAdmin
	]


admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment])
admin.site.register(Lesson, LessonAdmin)
