from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView
from django.views.generic.edit import FormView

from ProyectoJA import settings
from Users.forms import Usuario, RegisterForm, EditarNombreForm
from Users.models import User


class LoginUser(FormView):
    model = Usuario
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return render(request, self.get_success_url())
        else:
            return super(LoginUser, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect(self.get_success_url())


class LogoutUser(RedirectView):
    url = reverse_lazy('index')
    settings.LOGIN_URL = '/users/login/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LogoutUser, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutUser, self).get(request, *args, **kwargs)


def RegistrarUsuario(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            nuevousuario = form.save(commit=False)
            nuevousuario.Estado = 1
            nuevousuario.Tipo = 1
            nuevousuario.save()
            return redirect('/users/login/')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'users/formularioRegistro.html', context)


@login_required(login_url='/login')
def EditarNombre(request):
    usuario = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = EditarNombreForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('users:editar_nombre'))


    else:
        form = EditarNombreForm(instance=usuario)
        return render(request, "users/editNombre.html", {'form': form})


def borrarUsuario(request, id_usuario):
    usuarios = User.objects.get(id=id_usuario).delete()
    context = {'usuarios': usuarios}
    return redirect('/users/editarNombreMostrar/')
