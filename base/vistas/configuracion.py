
from django.shortcuts import render
from django.template import loader
import asyncio
import websockets

async def configuracion(request):
    uri = "ws://localhost:6789"
    hilos = None
    try:
        async with websockets.connect(uri) as websocket:
            hilos = await websocket.recv()  
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Conexion cerrada: {e}")
    except Exception as e:
        print(f"Error: {e}")

    context = {
        'hilos': hilos
    }
    return render(request, 'configuracion/configuracion.html', context)
