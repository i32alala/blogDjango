from django.conf.urls import patterns, url
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from blog.views import editCatMostrar,editCategorias


urlpatterns = [
    url(r'^new/', views.insertarNoticia, name = 'Noticia'),
    url(r'^(?P<noticias>\d+)$',views.mostrarNoticia, name = 'noticia'),
    #url(r'^editarCom/(?P<i_comentario>\d+)$', views.editCom, name ='EditarCom'),
    url(r'^editarCom',views.editComMostrar, name = 'EditarComentarios'),
    url(r'^editar/(?P<id_noticia>\d+)$',views.editNoticias, name = 'EditarNoticia'),    
    url(r'^editar',views.editMostrar, name = 'EditarNoticias'),
    url(r'^borrarCom/(?P<i_comentario>\d+)$', views.borrarComentarios, name= 'BorrarComentario'),
    url(r'^borrar/(?P<i_noticia>\d+)$',views.borrarNoticias, name = 'BorrarNoticias'),
    url(r'^newCat/', views.insertarCategoria, name = 'Cate'),
    url(r'^borrarCat/(?P<id_categoria>\d+)$',views.borrarCategoria, name = 'BorrarCategorias'),
    url(r'^editCat/(?P<id_categoria>\d+)$',editCategorias.as_view(), name = 'editCat'),
    url(r'^editCat',editCatMostrar.as_view(), name = 'editCat'),    
    #url(r'^editCat',views.editCatMostrar, name = 'editCat'),    
    url(r'^',views.index, name = 'index'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
