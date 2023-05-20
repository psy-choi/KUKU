from django.db import models

# Create your models here.
def photo_upload_path(instance):
    # 카테고리별로 저장될 경로를 반환하는 함수
    return f'pictures/{instance.category}/'
class Picture(models.Model):
    like = models.IntegerField(default=0)
    title = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    address = models.ImageField(upload_to=photo_upload_path)