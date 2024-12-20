from django import forms
from base.models import CanalAnalogicoCarga, AlarmaCargaSetpoint, CanalAnalogicoEH
from bootstrap_modal_forms.forms import BSModalModelForm

class PeriodoForm (forms.Form):
    end = forms.IntegerField()
    start = forms.IntegerField()

class FormEditarCanalCarga(BSModalModelForm):
    class Meta:
        model = CanalAnalogicoCarga
        fields = ['nombre', 'escala', 'unidad']

class FormEditarAlarmaCarga(BSModalModelForm):
    class Meta:
        model = AlarmaCargaSetpoint
        fields = ['tipo', 'valor', 'habilitada']
        
class FormEditarCanalEH(BSModalModelForm):
    class Meta:
        model = CanalAnalogicoEH
        fields = ['estado', 'escala']
