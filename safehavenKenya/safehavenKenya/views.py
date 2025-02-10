from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 

def about(request):
    return render(request, 'about.html')

def awareness(request):
    return render(request,'Awareness-Page.html')

def education(request):
    return render(request,'educationPage.html')

def getInvolved(request):
    return render(request,'Get-involved.html')

def reportIncident(request):
    return render(request, 'reportIncident.html')

def VolunteerForm(request):
    return render(request, 'volunteer-form')
