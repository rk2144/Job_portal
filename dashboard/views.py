from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
def proxy(request):
    if request.user.is_applicant:
        return redirect('applicant-dashboard')
    elif request.Users.is_recruiter:
        return redirect('recruiter-dashboard')
    else:
        return redirect('login')


def applicant_dashboard(request):
    return render('dashboard/applicant_dashboard.html')


def recruiter_dashboard(request):
    return render('dashboard/recruiter_dashboard.html')


def index(request):
    return render(request,'dashboard/index.html')

def elements(request):
    return render(request,'dashboard/elements.html')
def about(request):
    return render(request,'dashboard/about.html')

def blog(request):
    return render(request,"dashboard/blog.html")
def contact(request):
    return render(request,"dashboard/contact.html")

def job_details(request):
    '''servicedata=Service.objects.all()
    data={
        'servicedata':servicedata
    }'''
    return render(request,"dashboard/job_details.html")
def job_listing(request):
    return render(request,"jobs/jobs.html")
def register(request):
    form = UserCreationForm()
    return render(request,"users/register_applicant.html",{'form':form})
def login(request):
    return render(request,'users/login.html')
def blog(request):
    return render(request,'dashboard/blog.html')
def singal_blog(request):
    return render(request,"dashboard/single-blog.html")
def search(request):
    return render(request,"jobs/search.html")

