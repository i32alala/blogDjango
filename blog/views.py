from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from blog.models import Noticia, Categoria, User, Comentarios
from blog.forms import NoticiaForm, CategoriaForm, ComentarioForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.views.generic import ListView, View

from .forms import CategoriaForm


# Create your views here.
@login_required(login_url='/login')
def insertarNoticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.Autor_id = request.user.id
            formulario.save()
            for item in request.POST.getlist('Categoria'):
                formulario.Categoria.add(item)
            return redirect(reverse_lazy('index'))
    else:
        form = NoticiaForm()
    context = {'form': form}
    return render(request, 'blog/insertarNoticias.html', context)


@login_required(login_url='/login')
def insertarCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    context = {'form': form}
    return render(request, 'blog/insertarCategoria.html', context)


def mostrarNoticia(request, noticias):
    noticia_list = Noticia.objects.get(id=noticias)
    try:
        comentarios = Comentarios.objects.filter(Noticia=noticias)
    except Comentarios.DoesNotExist:
        comentarios = None
    autor = User.objects.all()[:5]
    categoria = Categoria.objects.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.Noticia = noticia_list
            formulario.save()
            context = {'form': formulario, 'noticia': noticia_list, 'categoria_index': categoria, 'autor_index': autor,
                       'comentarios': comentarios}
            print form
            return render(request, "blog/mostrarNoticia.html", context)
    else:
        form = ComentarioForm()
    context = {'form': form, 'noticia': noticia_list, 'categoria_index': categoria, 'autor_index': autor,
               'comentarios': comentarios}
    return render(request, "blog/mostrarNoticia.html", context)


def index(request):
    noticia_index = Noticia.objects.all().order_by('Fecha').reverse()
    autor = User.objects.all()[:5]
    categoria = Categoria.objects.all()

    paginator = Paginator(noticia_index, 2)

    try:
        page = int(request.GET.get('page', '1'))

    except:
        page = 1

    try:
        posts = paginator.page(page)

    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response('blog/content.html',
                              {'noticia_index': posts, 'categoria_index': categoria, 'autor_index': autor},
                              context_instance=RequestContext(request))


def categoria(request, cat):
    categoria = Categoria.objects.all()
    autor = User.objects.all()[:5]
    noticia_categoria = Noticia.objects.filter(Categoria__id=cat)

    paginator = Paginator(noticia_categoria, 1)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)

    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response('blog/content.html',
                              {'noticia_index': posts, 'categoria_index': categoria, 'autor_index': autor},
                              context_instance=RequestContext(request))


def autor(request, aut):
    autor = User.objects.all()[:5]
    categoria = Categoria.objects.all()
    noticia_autor = Noticia.objects.filter(Autor__id=aut)
    template = loader.get_template('blog/content.html')
    context = RequestContext(request,
                             {'noticia_index': noticia_autor, 'categoria_index': categoria, 'autor_index': autor})
    return HttpResponse(template.render(context))


@login_required(login_url='/login')
def editMostrar(request):
    noticias = Noticia.objects.filter(Autor__id=request.user.id)

    paginator = Paginator(noticias, 2)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response('blog/editMostrar.html', {'noticias': posts}, context_instance=RequestContext(request))


@login_required(login_url='/login')
def editNoticias(request, id_noticia):
    noticias = Noticia.objects.get(id=id_noticia, Autor__id=request.user.id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticias)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoticiaForm(instance=noticias)
    context = {'form': form}
    return render(request, 'blog/editNoticias.html', context)


class editCatMostrar(ListView):
    template_name = "blog/editCatMostrar.html"
    context_object_name = "categorias"
    model = Categoria
    paginate_by = 2


# @login_required(login_url = '/login')
# def editCatMostrar(request):
#	categorias = Categoria.objects.all()
#	
#	paginator = Paginator(categorias,2)
#	
#	try:
#		page = int(request.GET.get('page','1'))
#	except:
#		page = 1
#	try:
#		posts = paginator.page(page)
#		
#	except(EmptyPage, InvalidPage):
#		posts = paginator.page(paginator.num_pages)
#	
#	return render_to_response('blog/editCatMostrar.html',{'categorias': posts},context_instance = RequestContext(request))

@login_required(login_url='/login')
def editComMostrar(request):
    comentarios = Comentarios.objects.all()
    noticias = Noticia.objects.all()
    autor = User.objects.all()

    paginator = Paginator(comentarios, 2)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)

    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response('blog/editComMostrar.html', {'comentarios': posts, 'noticias': noticias, 'autor': autor},
                              context_instance=RequestContext(request))


# def editCom(request,i_comentario):
#	comentarios = Comentarios.objects.get(id = i_comentario)
#	if request.method == 'POST':
#		form = ComentarioForm(request.POST, instance=comentarios)
#		if form.is_valid():
#			form.save()
#			return redirect('index')
#	else:
#		form = ComentarioForm(instance = comentarios)
#	context = {'form':form}
#	return render(request,'blog/editCom.html',context)


class editCategorias(View):
	template_name = "blog/editCategorias.html"
    form_class = CategoriaForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form = self.form_class(id=self.kwargs['id_categoria'])
            form.save()
            return redirect('index')
        return render(request, self.template_name, {'form': form})


# @login_required(login_url = '/login')
# def editCategorias(request,id_categoria):
#	categorias = Categoria.objects.get(id = id_categoria)
#	if request.method == 'POST':
#		form = CategoriaForm(request.POST, instance=categorias)
#		if form.is_valid():
#			form.save()
#			return redirect('index')
#	else:
#		form = CategoriaForm(instance = categorias)
#	context = {'form':form}
#	return render(request,'blog/editCategorias.html',context)

@login_required(login_url='/login')
def borrarCategoria(request, id_categoria):
    categorias = Categoria.objects.get(id=id_categoria).delete()
    context = {'categorias': categorias}
    return redirect('/cate/editCat')


@login_required(login_url='/login')
def borrarNoticias(request, i_noticia):
    noticias = Noticia.objects.get(id=i_noticia).delete()
    context = {'noticias': noticias}
    return redirect('/noticia/editar')


@login_required(login_url='/login')
def borrarComentarios(request, i_comentario):
    comentarios = Comentarios.objects.get(id=i_comentario).delete()
    context = {'comentarios': comentarios}
    return redirect('/com/editarCom')


def search(request):
    if 'q' in request.GET:
        noticia_index = Noticia.objects.filter(Titulo__contains=request.GET['q'])
        categoria = Categoria.objects.all()
        autor = User.objects.filter()
        paginator = Paginator(noticia_index, 1)

        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1
        try:
            posts = paginator.page(page)

        except(EmptyPage, InvalidPage):
            posts = paginator.page(paginator.num_pages)
        buscar = request.GET.copy()
        return render_to_response('blog/content.html',
                                  {'query': buscar, 'noticia_index': posts, 'categoria_index': categoria,
                                   'autor_index': autor}, context_instance=RequestContext(request))

    else:
        noticias = Noticia.objects.all()
        categoria = Categoria.objects.all()
        autor = User.objects.filter()
        context = {'noticia_index': posts, 'categoria_index': categoria, 'autor_index': autor}
        return render(request, "blog/content.html", context)
