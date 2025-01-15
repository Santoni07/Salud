from django.shortcuts import redirect, render
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from django.contrib.auth import logout

from django.utils import timezone
from django.contrib.sessions.models import Session
from django.contrib import messages
@never_cache
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data  # Limpio los datos
            user = authenticate(request, username=cd['email'], password=cd['password'])  # Autenticación por email

            if user is not None:  # Si el usuario existe y está activo
                if user.is_active:
                    login(request, user)

                    # Obtener el perfil del usuario y imprimir el rol
                    profile = user.profile  # Asegúrate de que el usuario tenga un perfil relacionado
                    print("Usuario autenticado:", profile.rol)  # Imprimir el rol del perfil

                    # Redirigir según el rol del usuario
                    if profile.rol == 'medico':  # Verifica si el rol es médico
                        return redirect('medico_home')  # Cambia a la URL adecuada para médicos
                    elif profile.rol == 'general':  # Verifica si el rol es jugador
                        return redirect('registrar_persona')  # Cambia a la URL adecuada para jugadores
                    elif profile.rol == 'representante':
                        return redirect('representante_home')
                    elif profile.rol == 'jugador':
                        return redirect('menu_jugador')
                    else:
                        return redirect('home')  # Redirigir a una página predeterminada si no es médico ni jugador
                else:
                    return HttpResponse('El usuario no está activo')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos intente nuevmente.')
                return redirect('login')  # Redirige al login
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return redirect('persona/registrar')

@login_required
def check_session(request):
    # Verificar si la sesión ha expirado
    session = Session.objects.get(session_key=request.session.session_key)
    if timezone.now() - session.get_decoded().get('_session_expiry') > timezone.timedelta(seconds=900):
        return JsonResponse({'session_expired': True})
    else:
        return JsonResponse({'session_expired': False})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Guardar el usuario y su perfil
            user_form.save()  # Guarda tanto el usuario como el perfil asociado
            return render(request, 'account/register_done.html', {'new_user': user_form.cleaned_data['email']})
    else:
        user_form = UserRegistrationForm()

    # Mover este render fuera del bloque else, así se ejecuta tanto para GET como en caso de errores de validación
    return render(request, 'account/register.html', {'user_form': user_form})

def logout_view(request):
    logout
    return redirect('core/home.html')




def recover_Password(request):
    return render(request, 'account/password_change_form.html')