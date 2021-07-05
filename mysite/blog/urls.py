from . import views
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('', views.list_view, name='home'),
    path('<id>/', views.detail_view, name='detail_view' ),
    path('create', views.create_view, name='create_view'),
    path('update/<id>/', views.update_view, name='update_view'),
    path('delete/<id>/', views.delete_view, name='delete_view'),
    path('pesan_category/<id>/', views.pesan_category, name='pesan_category'),
    path('batalpesan_category/<id>/', views.batalpesan_category, name='batalpesan_category'),
]