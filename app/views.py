from django.shortcuts import render
from .models import ProfileDate,Tool,SocialLink

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
    profile = ProfileDate.objects.first()