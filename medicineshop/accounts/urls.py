from django.urls import path
from . import views
#from django.contrib.auth.views import login,logout,password_reset,password_reset_done,password_reset_confirm,password_reset_complete
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('', views.home, name="account_home"),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/', views.register, name= 'register'),
    path('profile/',views.view_profile, name='profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('change-password/',views.change_password,name='change_password'),
    #path('reset-password/',password_reset, name='reset_password'),
    #path('reset-password/done/', password_reset_done, name='password_reset_done'),
    #path('reset-password/confirm(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', password_reset_confirm, name='password_reset_confirm'),
    #path('reset-password/complete/', password_reset_complete, name='password_reset_complete'),
    path('(?P<category_slug>[-\w]+)/', views.product_list, name='product_list_by_category'),

    path('(?P<product_id>\d+)/(?P<slug>[-\w]+)/',views.product_detail,name='product_detail')

]
