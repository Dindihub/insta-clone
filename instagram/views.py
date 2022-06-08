
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateUserForm,ProfileForm,UpdateUserForm,ImageForm,CommentForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Profile,Image,Comment,Follow


# views for html
def index(request):
    
    return render(request, 'index.html')

def register(request):
    form=CreateUserForm

    if request.method =='POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,("registration successful"))
        
            return redirect('login')

    return render(request,'registration/register.html',{'form':form})

def login_user(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("login successful"))
            return redirect('home')
        
    context={}
    return render(request,'index.html',context)

def log_out(request):
    logout(request)
    return render(request,'index.html')



@login_required(login_url='login')
def home(request):
    images = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ImageForm()
    context = {
        'images': images,
        'form': form,
        'users': users,

    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def upload_photo(request):
    images = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = ImageForm()
    context = {
        'images': images,
        'form': form,
        'users': users,

    }
    return render(request, 'upload_photo.html', context)

@login_required(login_url='login')
def post_comment(request, id):
    image = get_object_or_404(Image, pk=id)
    is_liked = False
    if image.likes.filter(id=request.user.id).exists():
        is_liked = True
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.post = image
            savecomment.user = request.user.profile
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    context = {
        'image': image,
        'form': form,
        'is_liked': is_liked,
        'total_likes': image.total_likes()
    }
    return render(request, 'comment.html', context)
    

@login_required(login_url='login')
def profile(request):
    profiles=Profile.objects.get(user=request.user)
    images=Image.objects.filter(user=profiles)

             
    context={
        'images':images,
        'profiles':profiles 
        }
    
    return render(request,'profile.html',context )

@login_required(login_url='login')
def update_profile(request):
    profiles = Profile.objects.get(user=request.user)
    

        # print('profile2',profile)
    images = request.user.profile.images.all()
    if request.method == 'POST':
        # user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if  prof_form.is_valid():
            # user_form.save()
            prof_form.save()
            return redirect('profile')
            
            # return HttpResponseRedirect(request.path_info)
    else:
        # user_form = UpdateUserForm(instance=request.user)
        prof_form = ProfileForm(instance=request.user.profile)
             
    context={
        # 'user_form': user_form,
        'prof_form': prof_form,
        
        
        }
    
    return render(request, 'update_profile.html',context)





@login_required(login_url='login')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.images.all()
    
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
    context = {
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
    }
    print(followers)
    return render(request, 'user_profile.html', context)

@login_required(login_url='login')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'results.html', {'message': message})





