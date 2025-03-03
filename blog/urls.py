from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns =[
  path('', views.post_list, name='post_list'),
  path('post/<int:pk>', views.post_detail, name='post_detail'),
  path('post/new/', views.post_new, name='post_new'),
  path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
  path('register/', views.register, name='register'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('profile/', views.profile, name='profile'),
]