
from django.shortcuts import render
from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)
from django.urls import reverse_lazy
from base.forms import FormEditarCanalCarga, FormEditarCanalEH, FormEditarAlarmaCarga
from base.models import CanalAnalogicoEH, CanalAnalogicoCarga, AlarmaCargaSetpoint

class edit_canal_carga(BSModalUpdateView):
    model = CanalAnalogicoCarga
    template_name = 'modales/edit_canal_carga.html'
    form_class = FormEditarCanalCarga
    success_url = reverse_lazy('config_canales')  # Redirige después de guardar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse_lazy('edit_canal_carga', kwargs={'pk': self.object.pk})
        return context
    
class edit_alarma_carga(BSModalUpdateView):
    model = AlarmaCargaSetpoint
    template_name = 'modales/edit_alarma_carga.html'
    form_class = FormEditarAlarmaCarga
    success_url = reverse_lazy('config_canales')  # Redirige después de guardar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse_lazy('edit_alarma_carga', kwargs={'pk': self.object.pk})
        return context


class edit_canal_eh(BSModalUpdateView):
    model = CanalAnalogicoEH
    template_name = 'modales/edit_canal_eh.html'
    form_class = FormEditarCanalEH
    success_url = reverse_lazy('config_canales')  # Redirige después de guardar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = reverse_lazy('edit_canal_eh', kwargs={'pk': self.object.pk})
        return context