import random
import string
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    create_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.username



def unique_id():
    # Tạo một chuỗi ngẫu nhiên gồm 5 ký tự (chữ và số)
    characters = string.ascii_letters + string.digits
    id = ''.join(random.choice(characters) for _ in range(5))
    return id


class Blog(models.Model):
    id = models.CharField(max_length=5, primary_key=True, default=unique_id)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='imgs/', null=True)
    content = models.CharField(max_length=65536)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='blogs', null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        if not self.owner_id:
            self.owner = self._get_current_user()
        super().save(*args, **kwargs)
        
        
    def _get_current_user(self):
        # Lấy người dùng hiện tại (đăng nhập) thông qua hàm get_current_user()
        from django.contrib.auth import get_user
        return get_user()
