from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    # Head Module --------------------------------

    path('Head-Dashboard',views.head_dashboard,name='head_dashboard'),
    path('Head-Logout',views.head_logout,name='head_logout'),

    # Profile ------------------------------

    path('Profile',views.head_profile,name='head_profile'),
    path('Profile-Update',views.profile_detailsUpdate,name='profile_detailsUpdate'),
    path('Profile-Image\Remove',views.profileImage_remove,name='profileImage_remove'),

    # Password ----------------------------

    path('Password',views.head_password,name='head_password'),
    path('Password-Update',views.user_passwordUpdate,name='user_passwordUpdate'),
    

    #Schedule ----------------------------

    path('Schedule',views.head_schedule,name='head_schedule'),
    path('Head-Employees_schedule',views.head_employees_schedule,name='head_employees_schedule'),

    # Feedback  --------------------------

    path('Head-Feedback',views.head_feedback,name='head_feedback'),

    # Complaints --------------------------

    path('Head-Complaints',views.head_complaints,name='head_complaints'),

    # Action Taken  --------------------------

    path('Head-Action-Taken',views.head_actionTaken,name='head_actionTaken'),

    # Notification ----------------------

    path('Head-Notification',views.head_allnotification,name='head_allnotification'),

    # Leave ---------------------------
    
    path('Head-Leave',views.head_leave,name='head_leave'),

    
    

    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)