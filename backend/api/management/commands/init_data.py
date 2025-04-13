from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import Role, UserRole, MenuItem, RoleMenuAccess

class Command(BaseCommand):
    help = 'Initialize test data for the application'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating roles...')
        admin_role, _ = Role.objects.get_or_create(name='Admin', description='Full system access')
        user_role, _ = Role.objects.get_or_create(name='User', description='Basic access to content')
        
        self.stdout.write('Creating users...')
        # Create admin user if it doesn't exist
        try:
            admin_user = User.objects.get(username='admin')
        except User.DoesNotExist:
            admin_user = User.objects.create_user('admin', 'admin@example.com', 'admin')
        
        # Create regular user if it doesn't exist
        try:
            regular_user = User.objects.get(username='user')
        except User.DoesNotExist:
            regular_user = User.objects.create_user('user', 'user@example.com', 'user')
        
        self.stdout.write('Assigning roles to users...')
        UserRole.objects.get_or_create(user=admin_user, role=admin_role)
        UserRole.objects.get_or_create(user=regular_user, role=user_role)
        
        self.stdout.write('Creating menu items...')
        # L1 Menu Items
        dashboard, _ = MenuItem.objects.get_or_create(
            name='Dashboard',
            url='/dashboard',
            icon='LayoutDashboard',
            level=1,
            order=1
        )
        
        user_management, _ = MenuItem.objects.get_or_create(
            name='User Management',
            url='#',
            icon='Users',
            level=1,
            order=2
        )
        
        reports, _ = MenuItem.objects.get_or_create(
            name='Reports',
            url='#',
            icon='BarChart',
            level=1,
            order=3
        )
        
        # L2 Menu Items
        users, _ = MenuItem.objects.get_or_create(
            name='Users',
            url='/dashboard/users',
            icon='User',
            level=2,
            parent=user_management,
            order=1
        )
        
        roles, _ = MenuItem.objects.get_or_create(
            name='Roles',
            url='/dashboard/roles',
            icon='Shield',
            level=2,
            parent=user_management,
            order=2
        )
        
        sales_report, _ = MenuItem.objects.get_or_create(
            name='Sales Report',
            url='/dashboard/reports/sales',
            icon='DollarSign',
            level=2,
            parent=reports,
            order=1
        )
        
        user_report, _ = MenuItem.objects.get_or_create(
            name='User Report',
            url='/dashboard/reports/users',
            icon='Users',
            level=2,
            parent=reports,
            order=2
        )
        
        self.stdout.write('Assigning menu access to roles...')
        # Admin role has access to all menu items
        for menu_item in MenuItem.objects.all():
            RoleMenuAccess.objects.get_or_create(role=admin_role, menu_item=menu_item)
        
        # User role has access to dashboard only
        RoleMenuAccess.objects.get_or_create(role=user_role, menu_item=dashboard)
        
        self.stdout.write(self.style.SUCCESS('Successfully initialized test data'))