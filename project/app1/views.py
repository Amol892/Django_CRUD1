from django.shortcuts import redirect, render
from .forms import PersonForm
from .models import Person
import logging
# Create your views here.
logger = logging.getLogger("django")

def Person_view(request):
    template_name='app1/person.html'
    form=PersonForm()
    if request.method == 'POST':
        form=PersonForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            logger.info("New record is added")
            
            return redirect('home_url')
    context={'form':form}
    return render(request,template_name,context)

def Home_view(request):
    template_name='app1/home.html'
    obj=Person.objects.all()
    logger.info("All records are feteched and displayed on home page")
    context={'object':obj}
    return render(request,template_name,context)

def Update_view(request,pk=None):
    template_name = 'app1/update.html'
    obj=Person.objects.get(pk=pk)
    form=PersonForm(instance=obj)
    if request.method=='POST':
        form=PersonForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            logger.info("Record is updated")
            return redirect('home_url')
    context={'form':form}
    return render(request,template_name,context)

def Delete_view(request,pk=None):
    obj=Person.objects.get(pk=pk)
    obj.delete()
    logger.info("Record is deleted")
    return redirect('home_url')