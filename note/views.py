from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import notes


# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        register_username = request.POST['register_username']
        register_password = request.POST['register_password']
        register_confirm_password = request.POST['register_confirm_password']
        
        if register_password == register_confirm_password:
            if User.objects.filter(username = register_username).exists():
                messages.info(request,"USERNAME ALREADY EXSITS")
                return redirect('register')
            else:
                register_user = User.objects.create_user(username=register_username , password= register_password)
                register_user.save()
                return redirect('login')
        else:
            messages.info(request,"PASSWORD DOESN'T MATCH")
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    
    if request.method == 'POST':
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']
        login_user = auth.authenticate(username = login_username, password = login_password)
        if login_user is not None:
            auth.login(request,login_user)
            return redirect('index')
        else:
            messages.info(request,"WRONG USERNAME OR PASSWORD")
            return redirect('login')
    else:
        return render(request,'login.html')
    
@login_required(login_url='login') 
def index(request):
    get_username = request.user.username
    
    if request.method == 'POST':
        get_content = request.POST['note']
        notes.objects.create(check_username = get_username, content = get_content)
        return redirect('index')
    
    get_note = notes.objects.filter(check_username = get_username).order_by('-created_at')[:3]
    return render(request,'index.html',{'notes' : get_note})

def all_notes(request):
    username = request.user.username
    all_note = notes.objects.filter(check_username = username).order_by('-created_at')
    return render(request,'all_notes.html',{'all_note':all_note})

def delete(request,note_id):
    note = get_object_or_404(notes , id = note_id , check_username = request.user.username)
    note.delete()
    next_page = request.GET.get('next','all_notes')
    return redirect(next_page)

def go_back(request):
    return redirect("index")