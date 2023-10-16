from datetime import date, timedelta
from datetime import datetime
from django.shortcuts import render,redirect
from Registration_Login.models import *
from DM_Head.models import *
from django.http import HttpResponseRedirect, JsonResponse



def tl_dashboard(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'TL_dashboard.html',content)

    else:
            return redirect('/')
    

# Leave ------------------------------


def tl_leave(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        # employees = EmployeeRegister_Details.objects.filter(logreg_id.position =='Employee')
        employees = EmployeeRegister_Details.objects.filter(logreg_id__position="employee").exclude(logreg_id=emp_dash)
        print(employees)

        tl_leaves = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')
        employee_leaves = EmployeeLeave.objects.exclude(emp_id=dash_details).order_by('-id')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'tl_leaves':tl_leaves,
                   'employee_leaves':employee_leaves,
                   'employees':employees}

        return render(request,'TL_leave.html',content)

    else:
            return redirect('/')

def tl_leave_apply(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
            
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        if request.POST:
            from_date =  request.POST['from_date']
            to_date =  request.POST['to_date']
            type =  request.POST['type_select']
            reason =  request.POST['reason']
            current_date = date.today()

            start_date_str = request.POST['from_date']
            end_date_str = request.POST['to_date'] 

            # Convert the date strings to datetime objects
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

            # Calculate the difference in days
            weekdays_count = (count_weekdays(start_date, end_date))

            tl_leave = EmployeeLeave(emp_id=dash_details,
                                     start_date=from_date,
                                     end_date=to_date,
                                     leave_type=type,
                                     no_of_days=weekdays_count,
                                     leave_reason=reason,
                                     leave_apply_date=current_date)
            tl_leave.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    else:
            return redirect('/')
    
def count_weekdays(start_date, end_date):
    current_date = start_date
    weekdays_count = 0

    # Iterate through each date within the range
    while current_date <= end_date:
        # Check if the current date is a weekday (Monday to Saturday)
        if current_date.weekday() < 6:
            weekdays_count += 1
        
        # Move to the next day
        current_date += timedelta(days=1)

    return weekdays_count


def tl_filter_leaves(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
            
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')
        
        myleave = list(EmployeeLeave.objects.filter(emp_id=dash_details,start_date__range=[from_date, to_date]).values())

        return JsonResponse({'myleave': myleave})

def tl_filter_leaves_emp(request):
     if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
            
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        eid = request.GET.get('emp_id')
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')

        empleaves = EmployeeLeave.objects.exclude(emp_id=dash_details).filter(emp_id=eid,start_date__range=[from_date, to_date])

        leave_data = []
        for leave in empleaves:
            leave_dict = {
                'emp_name': leave.emp_id.emp_name,
                'start_date': leave.start_date,
                'end_date': leave.end_date,
                'no_of_days': leave.no_of_days,
                'leave_type': leave.leave_type,
                'leave_reason': leave.leave_reason,
                'leave_status': leave.leave_status,
            }
            leave_data.append(leave_dict)
        print(leave_data)

        return JsonResponse({'myleave': leave_data})
            
        

# Action Taken -------------------

def tl_actionTaken(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        employees = EmployeeRegister_Details.objects.filter(logreg_id__position="employee").exclude(logreg_id=emp_dash)
        action_taken_data = ActionTaken.objects.filter(act_from_id=dash_details.id)

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'action_taken_data':action_taken_data}

        return render(request,'TL_actionTaken.html',content)

    else:
            return redirect('/')
    
def tl_action_taken_save(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
            
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        if request.POST:
            emp_id = request.POST['action_employeeId']
            date =  request.POST['action_taken_date']
            head =  request.POST['reason_content_head']
            reason =  request.POST['reason_content']
            action =  request.POST['what_action_content']


            tl_action = ActionTaken(act_emp_id_id=emp_id,
                                     act_from_id=dash_details.id,
                                     act_from_name=dash_details.emp_name,
                                     act_reason=reason,
                                     act_head=head,
                                     act_content=action,
                                     action_date=date
                                     )
            tl_action.save()

            notification_obj = Notification()
            notification_obj.emp_id = dash_details 
            notification_obj.notific_head = "Action Taken" 
            notification_obj.notific_content = "Action has been taken by Team Lead" 
            notification_obj.save()


        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    else:
            return redirect('/')

def tl_action_taken_editPage(request,act_id):
     if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
            
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        employees = EmployeeRegister_Details.objects.filter(logreg_id__position="employee").exclude(logreg_id=emp_dash)
        action = ActionTaken.objects.get(id=act_id)
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'action':action,
                   'employees':employees }
        return render(request,'TL_actionTakenedit.html',content)
     

def tl_action_takenEdit(request,aid):
    print('edit')
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
            
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        action = ActionTaken.objects.get(id=aid)
        print(action)

        if request.POST:
            print('post')
            emp_id = request.POST['action_employeeId']
            date =  request.POST['action_taken_date']
            head =  request.POST['reason_content_head']
            reason =  request.POST['reason_content']
            action =  request.POST['what_action_content']


            action.act_emp_id_id=emp_id
            action.act_from_id=dash_details.id
            action.act_from_name=dash_details.emp_name
            action.act_reason=reason
            action.act_head=head
            action.act_content=action
            action.action_date=date
                                     
            action.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    else:
            return redirect('/')
     


# Feedback -------------------------

def tl_feedback(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        employees = EmployeeRegister_Details.objects.filter(logreg_id__position="employee").exclude(logreg_id=emp_dash)

        feedback_data = Feedback.objects.filter(from_id=dash_details.id).order_by('-id')
        print(feedback_data)

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'feedback_data':feedback_data}

        return render(request,'TL_feedback.html',content)

    else:
            return redirect('/')
    

def tl_add_feedback(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
            
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        if request.POST:
            emp_id = request.POST['emp_id']
            feedback =  request.POST['feedback']
            c_date = date.today()


            tl_feedback = Feedback(feedback_emp_id_id=emp_id,
                                     from_id=dash_details.id,
                                     from_name=dash_details.emp_name,
                                     feedback_content=feedback,
                                     feedback_date=c_date
                                     )
            tl_feedback.save()

            notification_obj = Notification()
            notification_obj.emp_id = dash_details 
            notification_obj.notific_head = "Feedback" 
            notification_obj.notific_content = "Feedback has been added by Team Lead" 
            notification_obj.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    else:
            return redirect('/')
     
def tl_filter_feedback(request):
     if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
            
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        eid = request.GET.get('emp_id')
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')

        print(eid)
        print(from_date)
        print(to_date)


        filter_feedback = Feedback.objects.filter(feedback_emp_id=eid,feedback_date__range=[from_date, to_date])
        print(filter_feedback)

        filter_data = []
        for f in filter_feedback:
            filter_dict = {
                'emp_name': f.feedback_emp_id.emp_name,
                'date': f.feedback_content,
                'feedback': f.feedback_date,
            }
            filter_data.append(filter_dict)
        print(filter_data)

        return JsonResponse({'filter_data': filter_data})    

# Complaints ---------------------

def tl_complaints(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        employees = EmployeeRegister_Details.objects.filter(logreg_id__position="employee").exclude(logreg_id=emp_dash)

        complaints_data = Complaints.objects.all()

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'complaints_data':complaints_data}

        return render(request,'TL_complaints.html',content)

    else:
            return redirect('/')
    

def tl_complaints_action_taken(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
            
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        if request.POST:
            cmp_id = request.POST['cmp_id']
            action =  request.POST['action_taken']
            c_date = date.today()

            complaint = Complaints.objects.get(id=cmp_id)

            complaint.action = action
            complaint.action_date = c_date

            complaint.save()

            notification_obj = Notification()
            notification_obj.emp_id = dash_details 
            notification_obj.notific_head = "Action Taken " 
            notification_obj.notific_content = "Action has been taken for the complaint by Team Lead" 
            notification_obj.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    else:
            return redirect('/')
     


# Profile Page -------------------------
def tl_profile(request):  
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'TL_profile.html',content)

    else:
            return redirect('/')
    

    
def tl_profile_detailsUpdate(request):
     
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')


        # Details Save -----------------

        if request.POST:
             
             emp_obj = EmployeeRegister_Details.objects.get(id=dash_details.id)

             emp_obj.emp_name = request.POST['empname']
             emp_obj.emp_contact_no = request.POST['contactno']
             emp_obj.emp_email = request.POST['empEmail']
             emp_obj.emp_address1 = request.POST['add1']
             emp_obj.emp_address2 = request.POST['add2']
             emp_obj.emp_address3 = request.POST['add3']
             emp_obj.emp_pin = request.POST['pincode']
             emp_obj.emp_location = request.POST['loc']
             emp_obj.emp_district = request.POST['empdist']
             emp_obj.emp_state = request.POST['empState']

             if request.FILES.get('empProfile'):
                emp_obj.emp_profile = request.FILES.get('empProfile')

             else:
                emp_obj.emp_profile =  emp_obj.emp_profile 

             if request.FILES.get('empResume'):
                emp_obj.emp_file = request.FILES.get('empResume')

             else:
                emp_obj.emp_file =  emp_obj.emp_file 

             emp_obj.save()
             success_text = 'Profile Details Updated.'
             success = True

             dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        
             content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'success_text':success_text,
                    'success':success}

        else:
            error_text = 'Profile Details Updated.'
            error = True
            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'error_text':error_text,
                    'error':error}

        return render(request,'TL_profile.html',content)

    else:
            return redirect('/')
    

# Remove Profile Image ---------------

def tl_profileImage_remove(request):
    emp_id = request.POST.get('emp_id')
    dash_details = EmployeeRegister_Details.objects.get(id=emp_id)
    dash_details.emp_profile = ''
    dash_details.save()
    return JsonResponse({'message': 'Received emp_id: ' + emp_id})
     
# End ------------------------------------------------


# Password Section -----------------------------------

def tl_password(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'TL_password.html',content)

    else:
            return redirect('/')


def tl_user_passwordUpdate(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        if request.POST:
           
           emp_dash.log_username = request.POST['emp_uname']
           emp_dash.log_password = request.POST['emp_password']

           emp_dash.save()  
           success = True
           success_text = 'User name or password change.'
        
           content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'success':success,
                   'success_text':success_text}
        else:

            error=True
            error_text = 'Oops! something went wrong.'
            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'error':error,
                    'error_text':error_text}

        return render(request,'TL_password.html',content)

    else:
            return redirect('/')


#Schedule -------------------------------------------

def head_schedule(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_dayTaskschedule.html',content)

    else:
            return redirect('/')
    

def head_employees_schedule(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_employees_dayTaskschedule.html',content)

    else:
            return redirect('/')
     


    

# Notification -----------------------


def tl_allnotification(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # dummy notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details).order_by('-notific_date')
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'TL_allnotification.html',content)

    else:
            return redirect('/')

def tl_open_notification(request,n_id):
     notification = Notification.objects.get(id=n_id)
     notification.notific_status = 1
     notification.save()
     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def tl_delete_notification(request,n_id):
     notification = Notification.objects.get(id=n_id)
     notification.delete()
     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
     
     

def tl_logout(request):
    request.session.pop('emp_id', None)
    return redirect('login_page')
