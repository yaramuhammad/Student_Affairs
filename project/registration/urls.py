from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),       #for the home page --> Default page when we run the server
    path('contact-us/',views.contact,name='contact'),
    path('department/',views.dept,name='dept'),
    path('update/',views.table_view,name='update'),
    path('registraion/',views.regist,name='regist'),
    path('search/',views.search,name='search'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', views.log_in, name='affairs-home'),
    path('logout/', views.log_out, name="log-out"),

    path('get_search/', views.get_search, name='get_search'),
    path('get_update/', views.get_update, name='get_update'),
    path('del_student/', views.del_student, name='del_student'),
    path('edit_student/', views.edit_student, name='edit_student'),
]


