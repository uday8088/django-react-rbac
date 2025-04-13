from django.contrib import admin
from .models import Role, UserRole, MenuItem, RoleMenuAccess

admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(MenuItem)
admin.site.register(RoleMenuAccess)