from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework.documentation import include_docs_urls
 #urls de la api con el router de rest_framework *nuevo*
router=routers.DefaultRouter()
router.register(r'apuntes',views.apuntesViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('docs/',include_docs_urls(title='Documentación de la API')), 
]