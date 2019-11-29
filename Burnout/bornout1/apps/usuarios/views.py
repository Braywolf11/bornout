from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.usuarios.forms import UsuariosForm
# Create your views here.
def indexusu(request):
    return render(request,'usuarios/index.html')

def usuario_view(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('index')
    else:
        form = UsuariosForm()
    return render(request, 'usuarios/usuarios_form.html', {'form': form})