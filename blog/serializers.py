from rest_framework import serializers
from .models import CustomUser, Blog


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'is_active', 'create_date']
        
        
class BlogSerializer(serializers.ModelSerializer):
    # lấy username của user chứ không lấy ID của user đó
    owner_username = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'owner_username', 'image']


class DetailSerializer(serializers.ModelSerializer):
    # lấy username của user chứ không lấy ID của user đó
    owner_username = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'owner_username', 'image', 'content']
