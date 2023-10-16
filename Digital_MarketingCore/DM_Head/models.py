from django.db import models
from  Registration_Login.models import EmployeeRegister_Details


class EmployeeSchedule(models.Model):
    emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    start_time = models.TimeField(auto_now=False,default='',null=True,blank=True)
    end_time = models.TimeField(auto_now=False,default='',null=True,blank=True)
    schedule_head = models.CharField(max_length=255,default='',null=True,blank=True)
    todo_content = models.TextField(default='',null=True,blank=True)
    log_time = models.TimeField(auto_now_add=True,null=True,blank=True)
    schedule_status = models.IntegerField(default=0)
    schedule_date = models.DateField(auto_now=False,null=True)


class Feedback(models.Model):
    feedback_emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    from_id = models.IntegerField(default=0)
    from_name = models.CharField(max_length=255,default='',null=True,blank=True)
    feedback_content = models.TextField(default='',null=True,blank=True)
    feedback_date = models.DateField(auto_now=False,null=True)

class Complaints(models.Model):
    complaint_emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    compaint_head = models.CharField(max_length=255,default='',null=True,blank=True)
    compaint_content = models.TextField(default='',null=True,blank=True)
    complaint_date = models.DateField(auto_now=True,null=True)
    action = models.TextField(default='',null=True,blank=True)
    action_date = models.DateField(auto_now=False,null=True)
    status = models.IntegerField(default=0)
    
class ActionTaken(models.Model):
    act_emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    act_from_id = models.IntegerField(default=0)
    act_from_name = models.CharField(max_length=255,default='',null=True,blank=True)
    act_reason = models.TextField(default='',null=True,blank=True)
    act_head = models.CharField(max_length=255,default='',null=True,blank=True)
    act_content = models.TextField(default='',null=True,blank=True)
    action_date = models.DateField(auto_now=False,null=True)
    status = models.IntegerField(default=0)


class Notification(models.Model):
    emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    notific_head = models.CharField(max_length=255,default='',null=True,blank=True)
    notific_content = models.TextField(default='',null=True,blank=True)
    notific_time = models.TimeField(auto_now_add=True,null=True,blank=True)
    notific_status = models.IntegerField(default=0)
    notific_date = models.DateField(auto_now=True,null=True)

class EmployeeLeave(models.Model):
    emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    start_date = models.DateField(auto_now=False,default='',null=True,blank=True)
    end_date = models.DateField(auto_now=False,default='',null=True,blank=True)
    leave_type = models.CharField(max_length=255,default='',null=True,blank=True)
    leave_reason = models.TextField(default='',null=True,blank=True)
    no_of_days = models.IntegerField(default=0)
    leave_status = models.IntegerField(default=0)
    leave_apply_date = models.DateField(auto_now=False,null=True)

class Allocation_Details(models.Model):
    allocatEmp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')
    allocat_to = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, related_name="EmployeeRegister", null=True,default='')
    allocate_status = models.IntegerField(default=0)
    alloaction_date = models.DateField(auto_now=False,null=True)


class Previos_Allocation_Details(models.Model):
    allocate_id = models.ForeignKey(Allocation_Details, on_delete=models.CASCADE, null=True,default='')
    previous_from_date = models.DateField(auto_now=False,null=True)
    previous_to_date = models.DateField(auto_now=False,null=True)
    previousemp_id = models.IntegerField(default=0)
    previousemp_name = models.CharField(max_length=255,default='',null=True,blank=True)
    previousemp_allocatedTo = models.IntegerField(default=0)
    previousemp_allocatedName = models.CharField(max_length=255,default='',null=True,blank=True)
    newallocation_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True,default='')