from django.urls import path
from . import views

urlpatterns = [
    path('signupapi',views.signup,name='signupapi'),
    path('loginapi',views.login,name='loginapi'),
    path('create', views.create_product, name='createapi'),
    path('list', views.list_products, name='retrieveapi'),
    path('listmed/<int:pk>', views.list_Medicine, name='retrieveapibyid'),
    path('update/<int:pk>', views.update_product, name='updateapi'),
    path('delete/<int:pk>', views.delete_product, name='deleteapi'),
    path('searchapi/<str:search>',views.search_med,name='searchmed'),
    path('logoutapi', views.logoutapi, name='logoutapi'),
]