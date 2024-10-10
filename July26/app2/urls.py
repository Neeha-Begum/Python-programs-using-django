from django.urls import path
from app2 import views
urlpatterns=[
    path('details',views.func1,name="d1"),
]