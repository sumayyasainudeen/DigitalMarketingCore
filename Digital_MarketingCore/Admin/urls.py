from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    #  Admin Module --------------------------------

    path('Admin-Dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('Admin-Logout',views.admin_logout,name='admin_logout'),

    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)