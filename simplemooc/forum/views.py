from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Thread, Replay
from .forms import ReplayForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#class ForumView(TemplateView):
    #template_name = 'forum/index.html'


class ForumView(ListView):
    
    paginate_by = 2
    template_name = 'forum/index.html'


    def get_queryset(self):
        queryset = Thread.objects.all()
        order = self.request.GET.get('order', '')
        if order == 'views':
            queryset = queryset.order_by('-views')
        elif order == 'answers':
            queryset = queryset.order_by('-answers')
        tag = self.kwargs.get('tag', '')
        if tag:
            queryset = queryset.filter(tags__slug__in=tag)    
        return queryset        

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        return context


class ThreadView(DetailView):
    queryset = Thread.objects.all()
    template_name = 'forum/thread.html'        

    def get(self, request, *args, **kwargs):
        response = super(ThreadView, self).get(request, *args, **kwargs)
        if not self.request.user.is_authenticated or \
            (self.object.author != self.request.user):
            self.object.views = self.object.views + 1
            self.object.save()
        return response    

    def get_context_data(self, **kwargs):
        context = super(ThreadView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        context['form'] = ReplayForm(self.request.POST or None)
        return context
    
    
    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request, 'Para responder ao Topico precisa estar logado!!'
            )
            return redirect(self.request.path)
        
        
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = context['form']
        if form.is_valid():
            replay = form.save(commit=False)
            replay.thread = self.object
            replay.author = self.request.user
            
            replay.save()
            messages.success(self.request, 'Resposta Enviada com Sucesso ')
            context['form'] = ReplayForm()

        return self.render_to_response(context)    

class ReplayCorrectView(View):
    correct = True

    def get(self, request, pk):
        replay = get_object_or_404(Replay, pk=pk, thread__author=request.user)
        replay.correct = self.correct
        replay.save()
        messages.success(request, 'Resposta Atualizada')
        return redirect(replay.thread.get_absolute_url())

index = ForumView.as_view()   
thread = ThreadView.as_view() 
replay_correct = ReplayCorrectView.as_view()
replay_incorrect = ReplayCorrectView.as_view(correct=False)