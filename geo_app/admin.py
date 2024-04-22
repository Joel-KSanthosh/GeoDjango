from django.contrib import admin
from .models import Points,Polygon,LineString
# Register your models here.

@admin.register(Points)
class PointsAdmin(admin.ModelAdmin):
    pass

@admin.register(LineString)
class LineAdmin(admin.ModelAdmin):
    pass

@admin.register(Polygon)
class PolygonAdmin(admin.ModelAdmin):
    pass
