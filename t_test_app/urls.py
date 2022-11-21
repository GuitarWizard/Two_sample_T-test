from django.urls import path
from t_test_app import views

urlpatterns = [path('',views.index, name='index')]
