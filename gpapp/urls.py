from gpapp import views
from django.urls import path


urlpatterns = [
    
    path('insert', views.insertFunc),  # Function views 방법
    path('insertprocess', views.insertprocessFunc),
    
    path('insert2', views.insertFunc2),
]