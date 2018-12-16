"""User views"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views

from users.forms import forms
from posts.models import Post
from users.models import Profile


# Models
from users.forms import ProfileForm, SignupForm



class UserDetailView(LoginRequiredMixin, DetailView):
	"""User detail view"""
	template_name = 'users/detail.html'
	slug_field = 'username'
	slug_url_kwarg = 'username' #como esta en route
	queryset = User.objects.all() #de donde obtiene la informacion
	context_object_name = 'user'
	
	def get_context_data(self, **kwargs):
		"""Añade los post del usuario"""
		context= super().get_context_data(**kwargs)
		user = self.get_object()
		context['posts'] = Post.objects.filter(user=user).order_by('-created')
		return context

class LoginView(auth_views.LoginView):
	"""Vista de autenticacion"""
	template_name = 'users/login.html'

#def login_view(request):
#	"""Login vista"""
#	if request.method == 'POST':
#		username = request.POST['username']
#		password = request.POST['password']
#		user = authenticate(request,username=username, password=password)
#		if user:
#			login(request,user)
#			return redirect('posts:feed')
#		else:
#			return render(request,'users/login.html',{'error':'Usuario invalido'})
#	return render(request,'users/login.html')

class LogoutView(auth_views.LogoutView):
	"""Vista de logout"""
	pass

#@login_required
#def logout_view(request):
#	"""Logout"""
#	logout(request)
#	return redirect('users:login')


class UserFormView(FormView):
	"""Crea perfil con Class View"""
	template_name= 'users/signup.html'
	form_class = SignupForm
	success_url = reverse_lazy('users:login')
	
	def form_valid(self, form):
		"""Salva la informacion del nuevo usuario"""
		form.save()
		return super().form_valid(form)


#def signup_view(request):
	#"""SIgnup"""
	#############################################
	#CODIGO CON UN MODELFORM
	#############################################
	#if request.method == 'POST':
	#	form = SignupForm(request.POST)
	#	if form.is_valid():
	#		form.save()
	#		return redirect('users:login')
	#else:
	#	form = SignupForm()
	#return render(request,'users/signup.html',context={'form':form})
        
	#############################################
	#CODIGO CON EL REQUEST
	#############################################	
	#	username = request.POST['username']
        #	passwd = request.POST['passwd']
        #	passwd_confirmation = request.POST['passwd_confirmation']

	 #       if passwd != passwd_confirmation:
          #  	    return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        #	try:
         #   		user = User.objects.create_user(username=username, password=passwd)
        #	except IntegrityError:
         #   		return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        #	user.first_name = request.POST['first_name']
        #	user.last_name = request.POST['last_name']
        #	user.email = request.POST['email']
        #	user.save()

        #	profile = Profile(user=user)
        #	profile.save()

        #	return redirect('login')

	#return render(request, 'users/signup.html')"""

class UserUpdateView(LoginRequiredMixin, UpdateView):
	"""Actualiza perfil con Class View"""
	template_name= 'users/update_profile.html'
	model = Profile
	fields = ['website','biography','phone_number','picture']

	def get_object(self):
		"""Regresa el perfil de usuario"""
		return self.request.user.profile
	
	def get_success_url(self, **kwargs):
		"""Crea la url de exito"""
		username = self.object.user.username
		return reverse('users:detail', kwargs={'username':username})


#@login_required
#def update_profile(request):
#	"""Update a user"""
#	profile = request.user.profile
#	if request.method == 'POST':
#		form = ProfileForm(request.POST, request.FILES)
#		if form.is_valid():
#			data = form.cleaned_data
#			profile.website = data ['website']
#			profile.phone_number = data ['phone_number']
#			profile.biography = data ['biography']
#			profile.picture = data ['picture']
#			profile.save()
#			#Redirige a una url fabricada
#			url = reverse('users:detail', kwargs={'username':request.user.username})
#			return redirect (url)
#	else:
#		form = ProfileForm()
#	return render(request, 'users/update_profile.html',context={
#		'profile':profile,
#		'user':request.user,
#		'form':form
#		})
