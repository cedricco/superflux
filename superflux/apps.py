from django.apps import AppConfig
from django.conf import settings
from django.contrib import admin
import django.contrib.admin.apps


class Config(AppConfig):
    name = "superflux"


class AdminConfig(django.contrib.admin.apps.AdminConfig):
    default_site = "superflux.apps.AdminSite"


class AdminSite(admin.AdminSite):
    site_header = "superflux"
    site_title = "superflux"
