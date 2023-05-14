from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Member
from .forms import MemberForm

# Create your views here.

def home(request):
    if request.method == 'POST':      
        form = MemberForm(request.POST)
        form.save()
        return redirect('content')
    form = MemberForm()
    context = {
        'form':form,
    }
    return render(request,'home.html',context)

def updateData(request, id):
    if request.method == 'POST':
        updData = Member.objects.get(id=id)
        form = MemberForm(request.POST, instance=updData)
        form.save()
        return redirect('content')
    else:
        updData = Member.objects.get(id=id)
        form = MemberForm(instance=updData)
    context={
        'id':id,
        'form':form,
    }
    return render(request,'update.html',context)
    

def deleteData(request, id):
    # delData = get_object_or_404(Member, pk=id)
    delData=Member.objects.get(id=id)
    delData.delete()
    return redirect('content')


def content(request):
    data = Member.objects.all()
    context = {
        'data': data
    }
    return render(request,'table.html',context)