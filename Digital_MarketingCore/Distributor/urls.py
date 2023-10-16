from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    #  Distributor Module --------------------------------

    path('Distributor-Dashboard',views.Distributor_dashboard,name='Distributor_dashboard'),
    path('Distributor-Logout',views.Distributor_logout,name='Distributor_logout'),

    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)