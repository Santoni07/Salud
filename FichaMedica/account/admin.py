from django.contrib import admin
from .models import Profile
from django.contrib import admin
from .models import Profile
from django.contrib.auth.hashers import make_password

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nombre', 'apellido', 'dni', 'fecha_nacimiento', 'email', 'rol')
    search_fields = ('user__username', 'nombre', 'apellido', 'email')
    list_filter = ('rol',)
    list_editable = ('rol',)

    def save_model(self, request, obj, form, change):
        if not obj.user.pk:  # Solo para nuevos usuarios
            obj.user.set_password(obj.user.password)  # Cifra la contraseña si es nueva
            obj.user.save()
        elif 'password' in form.changed_data:
            obj.user.password = make_password(obj.user.password)  # Cifra si se cambió la contraseña
            obj.user.save()
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('user')

admin.site.register(Profile, ProfileAdmin)