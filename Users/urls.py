from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

from Users.views import LoginUser

urlpatterns = patterns('',
	url(r'^login/$', LoginUser.as_view(), name = 'login'),
	#url(r'^logout/$', LogoutUser.as_view(), name = 'logout'),
	url(r'^salir/$', 'django.contrib.auth.views.logout', {'next_page': '/users/login'}, name="logout"),
	url(r'^new/$', 'Users.views.RegistrarUsuario', name = "new"),
	url(r'^editar_nombre/$', 'Users.views.EditarNombre', name='editar_nombre'),
	url(r'^borrarUsuario/(?P<id_usuario>\w{0,50})$', 'Users.views.borrarUsuario', name='borrarUsuario'),

) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
