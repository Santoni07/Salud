from django.views.generic.edit import FormView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.urls import reverse_lazy

class BaseExamenView(FormView):
    template_name = 'medico/medico_home.html'
    model = None  # Debes definir este campo en cada vista específica
    form_class = None  # Debes definir este campo en cada vista específica
    registro_medico_field = 'ficha_medica'  # Cambiar si el campo es diferente

    def dispatch(self, request, *args, **kwargs):
        self.jugador = get_object_or_404(Jugador, id=self.kwargs['jugador_id'])
        self.registro_medico = RegistroMedico.objects.filter(jugador=self.jugador).first()
        if not self.registro_medico:
            return JsonResponse({"error": "No se encontró el registro médico del jugador."}, status=404)
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return self.model.objects.filter(**{self.registro_medico_field: self.registro_medico}).first()

    def form_valid(self, form):
        with transaction.atomic():
            obj = form.save(commit=False)
            setattr(obj, self.registro_medico_field, self.registro_medico)
            obj.save()
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"success": True, "message": "Formulario guardado exitosamente."})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({"success": False, "errors": form.errors})
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jugador'] = self.jugador
        return context


class ElectroBasalView(BaseExamenView):
    model = ElectroBasal
    form_class = ElectroBasalForm
    success_url = reverse_lazy('medico_home')  # Ajusta la URL según sea necesario

class ElectroEsfuerzoView(BaseExamenView):
    model = ElectroEsfuerzo
    form_class = ElectroEsfuerzoForm
    success_url = reverse_lazy('medico_home')

class CardiovascularView(BaseExamenView):
    model = Cardiovascular
    form_class = CardiovascularForm
    success_url = reverse_lazy('medico_home')

class LaboratorioView(BaseExamenView):
    model = Laboratorio
    form_class = LaboratorioForm
    success_url = reverse_lazy('medico_home')

class ToraxView(BaseExamenView):
    model = Torax
    form_class = ToraxForm
    success_url = reverse_lazy('medico_home')

class OftalmologicoView(BaseExamenView):
    model = Oftalmologico
    form_class = OftalmologicoForm
    success_url = reverse_lazy('medico_home')

class OtrosExamenesClinicosView(BaseExamenView):
    model = OtrosExamenesClinicos
    form_class = OtrosExamenesClinicosForm
    success_url = reverse_lazy('medico_home')