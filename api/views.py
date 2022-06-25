from django.http import JsonResponse
from rest_framework.generics import ListAPIView,  get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.

def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)

class MenuSemanaListView(ListAPIView):
    queryset = MenuSemana.objects.all()
    serializer_class = MenuSemanaSerializers

class PlatoListView(ListAPIView):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializers

class PlatoDetail(APIView):
    def get(self, request, pk):
            plato = get_object_or_404(Plato,id=pk)
            if plato:
                serializer = PlatoSerializers(plato)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)    


class IngredienteDelete(APIView):
    def get(self, request, plato_id, ingrediente_id ):
        ingrediente = get_object_or_404(Ingrediente,id=self.kwargs['ingrediente_id'])
        if ingrediente:
            serializer = IngredienteSerializers(ingrediente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND) 

    
    def delete(self, request, plato_id, ingrediente_id): 
        plato = Plato.objects.filter(pk=self.kwargs['plato_id']).first()
        ingrediente = Ingrediente.objects.filter(pk=self.kwargs['ingrediente_id']).first()
        if plato:
            ingrediente.active = False
            ingrediente.save()
            serializer1 = PlatoSerializers(plato)
            serializer2 = IngredienteSerializers(ingrediente)
            return Response({'mesagge':'Ingrediente eliminado correctamente'})
        return Response({'error':'El ingrediente no es parte de este plato|'})
