from django.contrib import admin


# Register your models here.
from users.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	"""Administración de perfiles"""
	list_display = ('pk','user','phone_number','website','picture') #Lista de los elementos en el gestor
	list_display_links = ('pk','user') #Elementos que sirven para consulta
	list_editable = ('phone_number','website','picture') #Elementos modificables en la consulta general
	search_fields = ('user__email','user__first_name','user__last_name','phone_number') ##Campos de busqueda
	list_filter = ('created','modified','user__is_active','user__is_staff')  ##Filtros preexistentes a la derecha
	
	##Consulta del detalle con dos arreglos, el primero son los nombres y el segundo las variables
	fieldsets=(
		##Seccion profile todo en una línea
		('Profile',{
			'fields': (('user','picture'),),
		}),
		##Seccion extra_info con una linea para website y telefono y otra para biografia
		('Extra info',{
			'fields': (('website','phone_number'),('biography'),),
		}),
		('Metadata',{
			'fields': (('created','modified'),),
		}),
	)
	##Valores solo lectura
	readonly_fields = ('created','modified')

####INICIAN PASOS PARA QUE EL MENU DE ADMIN AGREGES EL PERFIL EN DJANGO ADMIN SITE###
class ProfileInline(admin.StackedInline):
	"""Creacion de usuarios dentro del formulario"""
	model = Profile
	can_delete = False
	verbose_name_plural= 'profiles'

class UserAdmin(BaseUserAdmin):
	inlines = (ProfileInline,)
	list_display = ('username','email','first_name','last_name','is_active','is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
####TERMINAN PASOS PARA QUE EL MENU DE ADMIN AGREGES EL PERFIL###
