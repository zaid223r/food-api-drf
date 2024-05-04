from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

patterns = [
    path('', views.food_list),
    path('<int:id>/', views.food_detail)
]

urlpatterns = format_suffix_patterns(patterns)