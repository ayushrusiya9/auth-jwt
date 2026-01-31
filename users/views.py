# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from .serializers import UserSerializer
# # from rest_framework import viewsets
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# # Create your views here.
class RegisterUser(APIView):
    """
    use to register user.

    """
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        """
        create user in database.
        """
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({'error': 'Missing required fields'}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({'message': f'User {user.username} created successfully'})

class LoginUser(APIView):
    """
    use to login user.

    """
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        """
        authenticate user.
        """

        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Missing required fields'}, status=400)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': f'User {user.username} logged in successfully'})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

class ProfileView(APIView):
    """
    use to get user profile.

    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        get user profile.
        """
        user = request.user
        return Response({
            "msg":"profile fetched successfully! jwt is working!",
            'username': user.username,
            'email': user.email,
        })