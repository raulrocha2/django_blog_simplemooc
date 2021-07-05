from django.contrib import admin

from .models import Thread, Replay


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title','__str__','slug', 'author', 'created', 'modified')
    search_fields = ['title', 'author__email', 'body']
    prepopulated_fields = {'slug':('title', 'author')}
    

class ReplayAdmin(admin.ModelAdmin):
    list_display = ['thread', 'author','correct', 'created', 'modified']
    search_fields = ['thread__title', 'author__email', 'replay']



admin.site.register(Thread, ThreadAdmin)
admin.site.register(Replay, ReplayAdmin)        
