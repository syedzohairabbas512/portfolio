from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from syed import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_all/', views.view_all, name='view_all'),
    path('add-project/', views.add_project, name='add-project'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

