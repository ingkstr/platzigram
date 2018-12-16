from django import forms
from posts.models import Post

class PostForm (forms.ModelForm):
	"""Clase de Post"""
	
	class Meta:
		"""Configuraciones del formulario"""
		model = Post
		fields = {'user','profile','title','photo'}
