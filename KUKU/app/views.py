from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Picture, Visitors
from django.http import HttpResponse
import json
import base64
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import random


# Create your views here.
def home(request):
    visitor = Visitors.objects.first()
    visitor.visited += 1
    visitor.save()

    return render(request, 'home.html')

def ranking(request):
    try:
        top_3_by_fm = Picture.objects.values('fm').annotate(total_likes=Sum('like')).order_by('-total_likes')[:3]
        print(top_3_by_fm)
        day_top3 = Picture.objects.filter(category='day').order_by('-like')[:3]
        night_top3 = Picture.objects.filter(category='night').order_by('-like')[:3]
        ipselenti_top3 = Picture.objects.filter(category='ipselenti').order_by('-like')[:3]
    except Exception as e:
        return render(request, 'ranking.html', {'need_data': True})
    return render(request, 'ranking.html', {'need_data': False, 'fm_top3' : top_3_by_fm ,'day_top3': day_top3, 'night_top3': night_top3, 'ipselenti_top3': ipselenti_top3})

def pictures(request, category, search):
    if category in ['ipselenti', 'day', 'night']:
        pictures = Picture.objects.filter(category=category)
        pictures = list(pictures)
        random.shuffle(pictures)
    else:
        pictures = Picture.objects.all()
        pictures = list(pictures)
        random.shuffle(pictures)

    if search != "None":
        pictures = [pic for pic in pictures if search in pic.title]
  
    
    return render(request, 'pictures.html', {'pictures': pictures})

@method_decorator(csrf_exempt)
def like(request, picture_id):
    if request.method == "POST":
        like_up = Picture.objects.get(pk=picture_id)
        like_count = like_up.like + 1
        like_up.like += 1
        like_up.save()
        response = {
            'like_count': like_count
        }
        return HttpResponse(json.dumps(response))
    
def post(request):
    if request.method == "POST":
        title=request.POST['title']
        phone=request.POST['phone']
        category=request.POST['category']
        photo=request.FILES.get('photo')
        fm=request.POST['fm']
        image_data = base64.b64encode(photo.read()).decode('utf-8')
        try:
            Picture.objects.create(
                title=title,
                phone=phone,
                category=category,
                address=image_data,
                fm = fm,
            )
        except Exception as e:
            return redirect('post')
        return redirect('pictures', 'all', None)
    return render(request, 'post.html')