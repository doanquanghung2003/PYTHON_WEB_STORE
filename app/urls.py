from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', views.search, name="search"),
    path('category/',views.category , name="category"),
    path('detail/',views.detail,name="detail"),
    
     #-- pass change --
    path("password_reset/",
         auth_views.PasswordResetView.as_view(
            template_name='app/password_reset.html',
            email_template_name='app/email.html',
            subject_template_name='app/title_email.txt'),
         name='password_reset'),    
    path("password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name='app/password_reset_done.html'),
        name='password_reset_done'),
    
    path("password_change/",
         auth_views.PasswordChangeDoneView.as_view(
            template_name='app/password_change.html'),
         name='password_change'),
    path("completed_password_change/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name='app/completed_password_change.html'),
        name='completed_password_change'),

    #...
]


