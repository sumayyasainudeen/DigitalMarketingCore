from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    # Head Module --------------------------------

    path('TL-Dashboard',views.tl_dashboard,name='tl_dashboard'),
    path('TL-Logout',views.tl_logout,name='tl_logout'),

    # Profile ------------------------------

    path('TL-Profile',views.tl_profile,name='tl_profile'),
    path('TL-Profile-Update',views.tl_profile_detailsUpdate,name='tl_profile_detailsUpdate'),
    path('TL-Profile-Image\Remove',views.tl_profileImage_remove,name='tl_profileImage_remove'),

    # Password ----------------------------

    path('TL-Password',views.tl_password,name='tl_password'),
    path('TL-Password-Update',views.tl_user_passwordUpdate,name='tl_user_passwordUpdate'),

    # Feedback  --------------------------

    path('TL-Feedback',views.tl_feedback,name='tl_feedback'),
    path('TL-Add-Feedback',views.tl_add_feedback,name='tl_add_feedback'),
    path('TL-Filter-Feedback',views.tl_filter_feedback,name='tl_filter_feedback'),

    # Complaints --------------------------

    path('TL-Complaints',views.tl_complaints,name='tl_complaints'),
    path('TL-Complaints-Action',views.tl_complaints_action_taken,name='tl_complaints_action_taken'),

    # Action Taken  --------------------------

    path('TL-Action-Taken',views.tl_actionTaken,name='tl_actionTaken'),
    path('TL-ActionTakenSave',views.tl_action_taken_save,name='tl_action_taken_save'),
    path('TL-ActionTakenEdit\<int:act_id>',views.tl_action_taken_editPage,name='tl_action_taken_editPage'),
    path('TL-ActionTakenEdit\<int:aid>',views.tl_action_takenEdit,name='tl_action_takenEdit'),

    # Leave ---------------------------
    
    path('TL-Leave',views.tl_leave,name='tl_leave'),
    path('TL-Leave-Apply',views.tl_leave_apply,name='tl_leave_apply'),
    path('TL-Filter-Leave',views.tl_filter_leaves,name='tl_filter_leaves'),
    path('TL-Filter-Leave-Emp',views.tl_filter_leaves_emp,name='tl_filter_leaves_emp'),

    # Notification ----------------------

    path('TL-Notification',views.tl_allnotification,name='tl_allnotification'),
    path('TL-Open-Notification\<int:n_id>',views.tl_open_notification,name='tl_open_notification'),
    path('TL-Delete-Notification\<int:n_id>',views.tl_delete_notification,name='tl_delete_notification'),

     #Schedule ----------------------------

    path('Schedule',views.head_schedule,name='head_schedule'),
    path('Head-Employees_schedule',views.head_employees_schedule,name='head_employees_schedule'),

    
    

    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)