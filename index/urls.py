from django.urls import path
from . import views
from .views import IndexView, result

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('result/', result, name='result')
]