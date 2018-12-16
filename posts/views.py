from django.shortcuts import render, redirect


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from posts.forms import PostForm
from posts.models import Post


class PostFeedView(LoginRequiredMixin, ListView):
	"""Regresa todas las publicaciones"""
	template_name = 'posts/feed.html'
	model = Post
	ordering = ('-created',)
	paginate_by = 30
	context_object_name= 'posts'


#@login_required
#def list_posts(request):
#    """Enlista posts"""
#    posts = Post.objects.all().order_by('-created')
#    return render(request,'posts/feed.html',{'posts':posts})

class PostCreateView(LoginRequiredMixin, CreateView):
    """Crea post con CreateView"""
    template_name='posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed') #Hasta que se ocupe
    
    def get_context_data(self, **kwargs):
            """Añade usuario y perfil al contexto"""
            context = super().get_context_data(**kwargs)
            context['user'] = self.request.user
            context['profile'] = self.request.user.profile
            return context
            

#@login_required
#def create_post(request):
#	"""Crea post"""
#	if request.method == 'POST':
#		form = PostForm(request.POST, request.FILES)
#		if form.is_valid():
#			form.save()
#			return redirect ('posts:feed')
#	else:
#		form = PostForm()
#	return render(request,'posts/new.html', context={'form':form,'user':request.user, 'profile':request.user.profile})

class PostDetailView(LoginRequiredMixin, DetailView):
    """Get detail of a post"""
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name= 'post'
    
