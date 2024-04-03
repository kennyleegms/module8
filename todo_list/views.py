from django.shortcuts import render
from . import forms , models

# Create your views here.
def home_page(request):

    if request.method == "GET":
        return render(request,"index.html",
                      {"registration_form":forms.registration_form,
                       "display_alls":models.table.objects.all(),
                       "add_or_update":"Add Task"
                       })
    
    elif request.method == "POST" and "post" in request.POST:
        if not request.POST.get("post"):
            forms.registration_form(request.POST).save()
            return render(request,"index.html",
                          {"registration_form":forms.registration_form,
                           "display_alls":models.table.objects.all(),
                           "add_or_update":"Add Task",
                           "message_id":f"Task ID: {models.table.objects.all()[len(models.table.objects.all())-1].id}",
                           "message_task_name":f"Task Name: {models.table.objects.all()[len(models.table.objects.all())-1].task_name}",
                           "message_category":f"Task Category: {models.table.objects.all()[len(models.table.objects.all())-1].category}",
                           "message_due_date":f"Task Due Date: {models.table.objects.all()[len(models.table.objects.all())-1].due_date}",
                           "message_success":"Created Successfully"                       
                           })
        else:
            forms.registration_form(request.POST,
                instance=models.table.objects.get(id=request.POST.get("post"))).save()
            return render(request,"index.html",
                          {"registration_form":forms.registration_form,
                           "display_alls":models.table.objects.all(),
                           "add_or_update":"Add Task",
                           "message_id":f"Task ID: {models.table.objects.get(id=request.POST.get('post')).id}",
                           "message_task_name":f"Task Name: {models.table.objects.get(id=request.POST.get('post')).task_name}",
                           "message_category":f"Task Category: {models.table.objects.get(id=request.POST.get('post')).category}",
                           "message_due_date":f"Task Due Date: {models.table.objects.get(id=request.POST.get('post')).due_date}",
                           "message_success":"Updated Successfully"
                           })
    
    elif request.method == "POST" and "delete" in request.POST:
        x = models.table.objects.get(id=request.POST.get("delete")).id
        y = models.table.objects.get(id=request.POST.get("delete"))
        y.delete()
        return render(request,"index.html",
                          {"registration_form":forms.registration_form,
                           "display_alls":models.table.objects.all(),
                           "add_or_update":"Add Task",
                           "message_id":f"Task ID: {x}",
                           "message_task_name":f"Task Name: {y.task_name}",
                           "message_category":f"Task Category: {y.category}",
                           "message_due_date":f"Task Due Date: {y.due_date}",
                           "message_success":"Deleted Successfully"
                           })
    
    else:
        return render(request,"index.html",
                          {"registration_form":forms.registration_form(instance=models.table.objects.get(id=request.POST.get("put"))),
                           "display_alls":models.table.objects.all(),
                           "add_or_update":"Update Task",
                           "primary_key":models.table.objects.get(id=request.POST.get("put"))
                           })
    
    