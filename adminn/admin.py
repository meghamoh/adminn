# from django.contrib import admin

from django.contrib import admin
from adminn.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'nationality', 'designation', 'is_staff', 'is_active')
    search_fields = ('email', 'full_name', 'nationality', 'designation')
    fieldsets = (
        (None, {
            'fields': ('email', 'full_name', 'nationality', 'designation', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Roles', {
            'fields': ('is_customer', 'is_service_provider', 'is_franchisee', 'is_dealer'),
        }),
    )

admin.site.register(User, UserAdmin)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User,Country_Codes
# from .models import OTP, Customer, Dealer, District, Franchise_Type, Franchisee, ServiceProvider, State

# # Register your models here.

# class UserAdmin(BaseUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('full_name',)}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('email', 'is_staff', 'is_superuser')
#     search_fields = ('email',)
#     ordering = ('email',)

# admin.site.register(User, UserAdmin)
# admin.site.register(Country_Codes)
# admin.site.register(Customer)
# admin.site.register(ServiceProvider)
# admin.site.register(Franchisee)
# admin.site.register(Franchise_Type)
# admin.site.register(Dealer)
# admin.site.register(OTP)
# admin.site.register(District)
# admin.site.register(State)


