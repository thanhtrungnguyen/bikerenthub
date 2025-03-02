# from django.db import models
#
# # Create your models here.
# from django.db import models
# from django.contrib.gis.db import models as gis_models
# import uuid
# from backend.common.models import BaseModel
# from domains.stations.models import Station  # Assume there is a Station model
# from django.utils.translation import gettext_lazy as _
#
# class BikeType(models.TextChoices):
#     STANDARD = 'standard', _('Standard')
#     ELECTRIC = 'electric', _('Electric')
#     CARGO = 'cargo', _('Cargo')
#
# class BikeStatus(models.TextChoices):
#     AVAILABLE = 'available', _('Available')
#     IN_USE = 'in_use', _('In Use')
#     MAINTENANCE = 'maintenance', _('Maintenance')
#     LOCKED = 'locked', _('Locked')
#
# class Bike(BaseModel):
#     station = models.ForeignKey(
#         Station,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name='bikes'
#     )
#     bike_type = models.CharField(
#         max_length=20,
#         choices=BikeType.choices,
#         default=BikeType.STANDARD
#     )
#     status = models.CharField(
#         max_length=20,
#         choices=BikeStatus.choices,
#         default=BikeStatus.AVAILABLE
#     )
#     battery_level = models.PositiveSmallIntegerField(
#         null=True,
#         blank=True,
#         help_text="Battery level for electric bikes (0-100)"
#     )
#     location = gis_models.PointField(
#         geography=True,  # Optimized for distance queries
#         null=True,
#         blank=True,
#         help_text="Current GPS location of the bike"
#     )
#     last_maintenance_at = models.DateTimeField(
#         null=True,
#         blank=True,
#         help_text="The last date this bike was maintained"
#     )
#
#     class Meta:
#         db_table = 'bikes'
#         indexes = [
#             models.Index(fields=['status']),
#             models.Index(fields=['bike_type']),
#         ]
#         constraints = [
#             models.CheckConstraint(
#                 check=models.Q(battery_level__gte=0, battery_level__lte=100),
#                 name='battery_level_range'
#             )
#         ]
#
#     def __str__(self):
#         return f"{self.get_bike_type_display()} - {self.get_status_display()} (ID: {self.id})"
