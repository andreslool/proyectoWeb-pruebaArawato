from django.urls import path
from proyecto_webapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('tienda/', views.tienda, name="tienda"),
    path('contacto/', views.contacto, name="contacto"),
    path('politica/', views.politica, name="politica"),
    path('aviso_legal/', views.aviso_legal, name="aviso_legal"),
    path('cookies/', views.cookies, name="cookies"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)