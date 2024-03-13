
from django.urls import path, include
from storeroom import views

urlpatterns = [
    path('login/',views.login_page,name="login" ),
    path('',views.signup_page,name="signup" ),
    path('home',views.home_page,name="home" ),
    path('addmedicine',views.Add_Medicine,name="addmed" ),
    path('editmedicine/<int:pk>',views.Edit_Medicine,name="editmed" ),
    path('deletemedicine/<int:pk>',views.Delete_Medicine,name="delmed" ),
    path('listmedicine',views.List_Medicine,name="listmed" ),
    path('logout',views.Logout_View,name="logout" ),
    path('storeroomapi/', include('storeroomapi.urls')), 
    path('list_products',views.list_medicine,name='list_products'),
]
