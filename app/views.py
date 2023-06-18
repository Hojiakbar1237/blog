from django.shortcuts import render
from .models import ProfileDate,Tool,SocialLink,About,Category,Project

# Create your views here.
def home(request):
    profile = ProfileDate.objects.first()
    tools = Tool.objects.all().order_by("order")
    social_links = SocialLink.objects.all().order_by("order")
    context ={
        "profile":profile, # bu 1 don aqaytarayapti malumot
        "tools":tools, # queryset(list)
        "social_links":social_links
                }

    return render(request,"index.html",context)

def about(request):
    about = About.objects.last()
    tools = Tool.objects.all().order_by("order")

    context = {
        "about": about,
        "tools":tools # stringdagi tools bu htmldagi tuls,
    }
    return render(request, "about-us.html",context)

def portfolio(request):
    categories = Category.objects.all()
    projects = Project.objects.all()

    context = {
        "categories":categories,
        "projects": projects,
    }
    return render(request, "portfolio.html",context)




