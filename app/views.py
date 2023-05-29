from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Member
from .forms import MemberForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .forms import SignUpForm,UserEditForm,AdminEditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



# def home(request):
#         if 
#         form = MemberForm(user=request.user)
#         context = {
#               'form':form,
#                 'name':request.user
#         }
#         return render(request,'home.html',context)
    
#         try:
#             form = MemberForm(user=request.user,data=request.POST)
#             if form.is_valid():
#                 data=form.save(commit=False)
#                 data.user=request.user
#                 form.save()
#                 return redirect("content")
#             else:
#                 return redirect("home")
#         except Exception as e:
#             return HttpResponse(f"An error occurred: {str(e)}")


def home(request):
    context={}
    form = MemberForm(user=request.user,data=request.POST or None)
    ip = request.session.get('ip',0)
    if request.method == 'POST':      
        try:
            if form.is_valid():
                data=form.save(commit=False)
                data.user=request.user
                form.save()
                return redirect('content')
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")
    
    context['form']=form
    context['ip']=ip
    return render(request,'home.html',context)


@login_required()
def updateData(request, id):
    if request.method == 'POST':
        updData = Member.objects.get(id=id)
        form = MemberForm(data=request.POST, instance=updData)
        if form.is_valid():
            form.save()
            return redirect('content')
    else:
        updData = Member.objects.get(id=id)
        form = MemberForm(user=request.user,instance=updData)
    context={
        'id':id,
        'form':form,
    }
    return render(request,'update.html',context)
    

@login_required()
def deleteData(request, id):
    # delData = get_object_or_404(Member, pk=id)
    delData=Member.objects.get(id=id)
    delData.delete()
    return redirect('content')



def content(request):
    if request.user.is_authenticated:
        data = Member.objects.filter(user=request.user)
        if request.user.is_superuser == True:
            data = Member.objects.all()
            print("data",type(data),data)
        context = {
            'data': data
        }
        return render(request,'table.html',context)
    else:
        return render(request,'table.html')

# login view function
def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Logged In Sucessfully')
                    return redirect('content')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('content')
    
# Signup view function
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account created!')
            user = form.save()
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

#logout
@login_required()
def logout_user(request):
    logout(request)
    return redirect('login')

#change password while logged in
@login_required()
def change_pass_logged_in(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user) # Doesnt log out when password is changed
            messages.success(request,"Password channged sucessfully !")
            return redirect('contents')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'change_password.html',{'form':form})
class Api_create(APIView):
    @login_required
    def get(self,request):
        print("hello")
        data={'name':'Ram','age':20}
        return Response(data)
    
