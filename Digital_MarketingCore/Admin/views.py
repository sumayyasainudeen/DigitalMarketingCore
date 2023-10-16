from django.shortcuts import render,redirect
from Registration_Login.models import *



def admin_dashboard(request):
    if 'admin_id' in request.session:
        if request.session.has_key('admin_id'):
            admin_id = request.session['admin_id']
           
        else:
            return redirect('/')
        
        Admin_dash = LogRegister_Details.objects.get(id=admin_id)
        dash_details = BusinessRegister_Details.objects.get(log_id=Admin_dash)
        
        content = {'Admin_dash':Admin_dash,'dash_details':dash_details}

        return render(request,'AD_dashboard.html',content)

    else:
            return redirect('/')
    

def admin_logout(request):
    request.session.pop('admin_id', None)
    return redirect('login_page')
     


