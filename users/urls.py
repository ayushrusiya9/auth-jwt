from django.urls import path,include
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # path('', include(router.urls)),
    path('register/',views.RegisterUser.as_view(),name='register'),
    path('login/',views.LoginUser.as_view(),name='login'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
]
