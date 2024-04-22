from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class Points(models.Model):
    name = models.CharField(max_length=25)
    point = gis_models.PointField(srid=4326)

    def __str__(self):
        return self.name


class LineString(models.Model):
    name = models.CharField(max_length=25)
    lines = gis_models.LineStringField(srid=4326)
    point = models.ForeignKey(Points,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Polygon(models.Model):
    name = models.CharField(max_length=25)
    polygon = gis_models.PolygonField(srid=4326)
    lines = models.ForeignKey(LineString,on_delete=models.CASCADE)

    def __str__(self):
        return self.name