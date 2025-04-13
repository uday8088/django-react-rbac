from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Role, UserRole, MenuItem, RoleMenuAccess
from .serializers import UserSerializer, RoleSerializer, MenuItemSerializer, RoleMenuAccessSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class RoleMenuAccessViewSet(viewsets.ModelViewSet):
    queryset = RoleMenuAccess.objects.all()
    serializer_class = RoleMenuAccessSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    if user:
        # Get user roles
        user_roles = UserRole.objects.filter(user=user).values_list('role__name', flat=True)
        
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'roles': list(user_roles)
        })
    else:
        return Response({'error': 'Invalid credentials'}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_menu(request):
    # Get user roles
    user_roles = UserRole.objects.filter(user=request.user).values_list('role_id', flat=True)
    
    # Get menu items accessible by user roles
    menu_item_ids = RoleMenuAccess.objects.filter(role_id__in=user_roles).values_list('menu_item_id', flat=True)
    
    # Get L1 menu items
    l1_menu_items = MenuItem.objects.filter(id__in=menu_item_ids, level=1).order_by('order')
    l1_serializer = MenuItemSerializer(l1_menu_items, many=True)
    
    # Get L2 menu items
    l2_menu_items = MenuItem.objects.filter(id__in=menu_item_ids, level=2).order_by('parent_id', 'order')
    l2_serializer = MenuItemSerializer(l2_menu_items, many=True)
    
    return Response({
        'l1_menu_items': l1_serializer.data,
        'l2_menu_items': l2_serializer.data
    })