from django.urls import path
from employees import views

urlpatterns = [
    path('',views.index, name='indexpage') ### indexpage
]