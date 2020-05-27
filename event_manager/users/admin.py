from django.contrib import admin
from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = 'Event Manager administration'
    site_title = 'Event Manager admin'

    login_template = 'admin/login.html'


admin_site = MyAdminSite(name='myadmin')
