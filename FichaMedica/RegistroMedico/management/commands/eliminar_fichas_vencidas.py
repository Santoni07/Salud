from django.core.management.base import BaseCommand
from django.utils.timezone import now
from RegistroMedico.models import RegistroMedico

class Command(BaseCommand):
    help = "Elimina automáticamente las fichas médicas vencidas"

    def handle(self, *args, **kwargs):
        hoy = now().date()
        fichas_vencidas = RegistroMedico.objects.filter(fecha_caducidad__lt=hoy)

        if fichas_vencidas.exists():
            cantidad = fichas_vencidas.count()
            fichas_vencidas.delete()
            self.stdout.write(self.style.SUCCESS(f"✅ {cantidad} fichas médicas vencidas eliminadas correctamente."))
        else:
            self.stdout.write(self.style.WARNING("⚠️ No hay fichas médicas vencidas para eliminar."))

