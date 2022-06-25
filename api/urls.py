from django.urls import path
from .views import *

urlpatterns = [
    path('ping/', ping, name="ping"),
    path('menu/', MenuSemanaListView.as_view()),
    path('menu/platos', PlatoListView.as_view()),
    path('menu/platos/<int:pk>/', PlatoDetail.as_view()),
    path('menu/platos/<plato_id>/ingrediente/<ingrediente_id>/', IngredienteDelete.as_view()),
]