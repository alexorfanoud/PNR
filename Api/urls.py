from django.urls import path
from .views import ApiIndexView, ScenarioDetailView, PKDetailView, ModelDetailView , SectorDetailView, AvgByModelAndVariable

urlpatterns = [
    path('', ApiIndexView.as_view()),
    path('pk/<int:key>', PKDetailView.as_view()),
    path('scenario/<str:scenario>', ScenarioDetailView.as_view()),
    path('model/<str:model>', ModelDetailView.as_view()),
    path('section/<str:section>', SectorDetailView.as_view()),
    path('avg/<str:scenario>', AvgByModelAndVariable.as_view()),
]