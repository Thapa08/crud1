from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DropdownForm
# Create your views here.
@login_required
def dropdown(request):
    form = DropdownForm()
    context={
        'form':form,
    }
    return render(request,'dropdown.html',context)
