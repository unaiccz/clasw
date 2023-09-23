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
    path('apuntes/<int:pk>/delete/',views.apuntesDelete.as_view()),
    path('apuntes/<int:pk>/update/',views.apuntesUpdate.as_view()),
    path('apuntes/create/',views.apuntesCreate.as_view()),
    
]