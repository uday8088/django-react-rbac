from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RoleViewSet, MenuItemViewSet, RoleMenuAccessViewSet, login_view, get_user_menu

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'role-menu-access', RoleMenuAccessViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('user-menu/', get_user_menu, name='user-menu'),
]