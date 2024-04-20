from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('predict',views.predict,name="predict"),
    path('new_login', views.new_login, name="new_login"),
    path('new_logout', views.new_logout, name="new_logout"),
    path('new_contact', views.new_contact, name="new_contact"),
    path('new_register', views.new_register, name="new_register"),
    path('new_department', views.new_department, name="new_department"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('record',views.record,name='record'),
    path('xray',views.xray,name='xray'),
    path('diabetes',views.diabetes,name='diabetes'),
    path('chest_ct2',views.chest_ct2,name='chest_ct2'),
    path('chatbot', views.chatbot, name="chatbot"),

]