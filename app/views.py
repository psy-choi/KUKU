from django.shortcuts import render, redirect
from .models import Picture
from django.http import HttpResponse
import json

# Create your views here.
def home(request):
    return render(request, 'home.html')

def ranking(request):
    try:
        day_top3 = Picture.objects.filter(category='day').order_by('-like')[:3]
        night_top3 = Picture.objects.filter(category='night').order_by('-like')[:3]
        ipselenti_top3 = Picture.objects.filter(category='ipselenti').order_by('-like')[:3]
    except Exception as e:
        return redirect(request, 'ranking.html', {'need_data': True})
    return render(request, 'ranking.html', {'need_data': False, 'day_top3': day_top3, 'night_top3': night_top3, 'ipselenti_top3': ipselenti_top3})

def pictures(request, category, search):
    if category in ['ipselenti', 'day', 'night']:
        pictures = Picture.filter(category=category)
    else:
        pictures = Picture.all()
    
    if search:
        pictures = pictures.filter(title__contains=search)
    return render(request, 'pictures.html', {'pictures': pictures})

def like(request, picture_id):
    if request.method == "POST":
        like_up = Picture.objects.filter(pk=picture_id).update(
            like=like+1
            )
        like_count = like_up.like + 1
        response = {
            'like_count': like_count
        }
        return HttpResponse(json.dumps(response))
    
def post(request):
    if request.method == "POST":
        title=request.POST['title']
        phone=request.POST['phone']
        category=request.POST['category']
        address=request.FILES['picture']
        
        Picture.objects.create(
            title=title,
            phone=phone,
            category=category,
            address=address,
        )
        return redirect('pictures')