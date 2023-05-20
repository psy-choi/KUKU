from django.shortcuts import render, redirect
from .models import Picture, Visitors
from django.http import HttpResponse
import json
import base64
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
def home(request):
    visitor = Visitors.objects.first()
    visitor.visited += 1
    visitor.save()

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
    print(Picture.objects.all())
    if category in ['ipselenti', 'day', 'night']:
        pictures = Picture.objects.filter(category=category)
    else:
        pictures = Picture.objects.all() # 바꿈
    print(search)
    if search != "None":
        pictures = pictures.filter(title__contains=search)
  
    
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
        image_data = base64.b64encode(photo.read()).decode('utf-8')
        Picture.objects.create(
            title=title,
            phone=phone,
            category=category,
            address=image_data,
        )
        return redirect('pictures', 'all', None)
    return render(request, 'post.html')