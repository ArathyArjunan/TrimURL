from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('shorten/', views.create_short_link, name='create'),
    path('my-links/', views.get_user_links, name='my_links'),
    path('<str:code>/', views.redirect_to_original, name='redirect'),
     path('', views.frontend, name='frontend'),
]
