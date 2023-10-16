from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    # Super Admin Module --------------------------------

    path('Super-Admin-Dashboard',views.supper_admin_dashboard,name='supper_admin_dashboard'),
    path('Super-Admin-Logout',views.super_admin_logout,name='super_admin_logout'),

    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)