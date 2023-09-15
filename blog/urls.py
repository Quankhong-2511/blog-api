from django.urls import path
from .views import BlogAPIView, CustomUserAPIView, DetaiAPIView





urlpatterns = [
    
    path('blog/', BlogAPIView.as_view()),
    path('blog/<str:pk>/', DetaiAPIView.as_view()),
    path('user/', CustomUserAPIView.as_view()),
]

