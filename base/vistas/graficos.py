from base.forms import PeriodoForm
from base.models import Transitorio
from django.shortcuts import render

import plotly.express as px

def vista_graficos(request):
    trans = Transitorio.objects.all()[:1200]

    start = request.GET.get('start')
    end = request.GET.get('end')
    if(end):
        trans = trans[:end]
    if(start):
        trans = trans[start:]
    # print([(c.ia, c.ib) for c in trans][0:5])


    figa = px.line(
        x = range(0, len(trans)),
        y = [[c.va for c in trans],[c.vb for c in trans],[c.vc for c in trans]],
        labels={
            "x": "Muestra",
            "y": "V",
                 },
        title="Tensión"
    )
    figa.update_layout(
        height=180,
        margin=dict(l=5, t=25, b=5, r=5),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        font_size=8,
    )
    figa.update_xaxes(showline=True, linewidth=1, linecolor='black')
    figa.update_yaxes(showline=True, linewidth=1, linecolor='black')
    
    figb = px.line(
        x = range(0, len(trans)),
        y = [[c.ia for c in trans],[c.ib for c in trans],[c.ic for c in trans]],
        labels={
            "x": "Muestra",
            "y": "A",
                 },
        title="Corriente"
    )
    figb.update_layout(
        height=180,
        margin=dict(l=5, t=25, b=5, r=5),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        font_size=8,
    )
    figb.update_xaxes(showline=True, linewidth=1, linecolor='black')
    figb.update_yaxes(showline=True, linewidth=1, linecolor='black')

   

    form = PeriodoForm()
    context = {'figa':figa.to_html(), 'figb': figb.to_html(), 'form': form}
    return context
