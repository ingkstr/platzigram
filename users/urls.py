"""users urls"""

from django.urls import path


from users import views

urlpatterns = [
	path(
		route='<str:username>/',
		view=views.UserDetailView.as_view(),
		name='detail',
	),
	#path('users/login/',views.login_view, name='login'),
	path(
		route='users/login/',
		view=views.LoginView.as_view(),
		name='login',
	),
	path(
		route='users/logout/',
		view=views.LogoutView.as_view(),
		name='logout',
	),
	#path('users/logout/',views.logout_view, name='logout'),
	path(
		route='users/signup/',
		view=views.UserFormView.as_view(),
		name='signup',
	),
	#path('users/signup/',views.signup_view,name='signup'),
	path(
		route='users/me/profile/',
		view=views.UserUpdateView.as_view(),
		name='update_profile',
	),
	#path('users/me/profile',views.update_profile, name='update_profile'),
	]
