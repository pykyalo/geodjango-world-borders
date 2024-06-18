from django.contrib.gis.db import models

class WorldBorder(models.Model):
    """ ogrinfo -so world/data/TM_WORLD_BORDERS-0.3.shp TM_WORLD_BORDERS-0.3
    
    Gives:
    FIPS: String (2.0)
    ISO2: String (2.0)
    ISO3: String (3.0)
    UN: Integer (3.0)
    NAME: String (50.0)
    AREA: Integer (7.0)
    POP2005: Integer64 (10.0)
    REGION: Integer (3.0)
    SUBREGION: Integer (3.0)
    LON: Real (8.3)
    LAT: Real (7.3)
    """
    
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField("Population 2005")
    fips = models.CharField("FIPS Code", max_length=2, null=True, blank=True)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField("United Nations Code")
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()

    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name