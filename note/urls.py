from django.urls import path
from . import views
urlpatterns=[
  path('',views.index,name= 'index'),
  path('register',views.register,name='register'),
  path('login',views.login,name='login'),
  path('all_notes',views.all_notes,name='all_notes'),
  path('delete/<int:note_id>/',views.delete,name="delete"),
  path('go_back',views.go_back,name="go_back"),
 ]