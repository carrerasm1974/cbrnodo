
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from base.models import OperacionesCbr, MuestrasICbr, Category
from channels.db import database_sync_to_async
import plotly.express as px
import pandas as pd
from datetime import timedelta

def get_category_tree():
    def build_tree(node):
        return {
            'id': node.id,
            'name': node.name,
            'children': [build_tree(child) for child in node.children.all()]
        }

    root_categories = Category.objects.filter(parent__isnull=True)
    return [build_tree(root) for root in root_categories]

@database_sync_to_async
def operaciones_cbr(request): 

    categories = get_category_tree()

    operaciones = OperacionesCbr.objects.all()

    # Verificar si se ha seleccionado una operación
    operacion_id = request.GET.get('operacion_id')
    ia = None
    ib = None

    if operacion_id:
        operacion = get_object_or_404(OperacionesCbr, id=operacion_id)
        muestras = MuestrasICbr.objects.filter(op_id_id=operacion)
        if muestras.exists():
            df = pd.DataFrame(list(muestras.values()))
            df['ts'] = [ operacion.ts + timedelta(milliseconds=(x-200)*operacion.tsample) for x in range(len(df))] 
            fig = px.line(df, x='ts', y=['v0'], height=300)
            fig.update_layout(
                plot_bgcolor='white'
            )
            fig.update_xaxes(gridcolor='lightgrey')
            fig.update_yaxes(gridcolor='lightgrey')
            ia = fig.to_html(full_html=False)

            fig = px.line(df, x='ts', y=['v1'], height=300)
            fig.update_layout(
                plot_bgcolor='white'
            )
            fig.update_xaxes(gridcolor='lightgrey')
            fig.update_yaxes(gridcolor='lightgrey')
            ib = fig.to_html(full_html=False)


        else:
            ia = "<p>No hay datos de muestras para esta operación.</p>"

    context = {
        'operaciones': operaciones,
        'ia': ia,
        'ib': ib,
        'categories': categories
    }
    return render(request, 'operaciones_cbr/operaciones_cbr.html', context)
