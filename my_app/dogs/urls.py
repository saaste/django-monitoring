from django.urls import path
from . import views

app_name = 'dogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.details, name='details'),
    path('clean/', views.clean, name='clean')
]