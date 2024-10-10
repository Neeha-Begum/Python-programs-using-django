from django.urls import path
from app1 import views

urlpatterns=[
    path('num',views.func1,name="p1"),
    path('prime',views.func2,name="n1"),
    path('greatest',views.func3,name="g1"),
    path('armstrong',views.func4,name='a1'),
    path('hi',views.func5,name="h1")
]