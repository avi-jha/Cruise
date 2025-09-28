from django.contrib import admin

from authentication.models import Customer, LoginActivity

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'date_of_birth', 'gender')
    search_fields = ('user__username', 'phone', 'gender')


@admin.register(LoginActivity)
class LoginActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'login_time', 'logged_out')
    search_fields = ('user__username', 'ip_address')