from django.urls import path
from . import views

app_name = 'docs'

urlpatterns = [
    path('app_docs/', views.app_docs, name='app_docs'),
]