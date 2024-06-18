from django.contrib.gis import admin
from .models import WorldBorder


class WorldBorderAdmin(admin.ModelAdmin):
    list_display = ["name", "fips", "iso2", "iso3", "region", "subregion", "mpoly"]
    search_fields = ("name", "fips", "iso2", "iso3")

admin.site.register(WorldBorder, admin.GISModelAdmin)