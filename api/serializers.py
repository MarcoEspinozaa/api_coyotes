from rest_framework import serializers
from .models import *

class IngredienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id','name','active')
        

class PlatoSerializers(serializers.ModelSerializer):
    ingredientes = IngredienteSerializers(many=True, read_only=True)
    #ingredientes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Plato
        fields = ('id','name','ingredientes')
    


class MenuSerializers(serializers.ModelSerializer):
    plato = PlatoSerializers()
    class Meta:
        model = Menu
        fields = ('name','description','plato')


class MenuSemanaSerializers(serializers.ModelSerializer):
    menu = MenuSerializers()
    class Meta:
        model = MenuSemana
        fields = ('title','menu')



    