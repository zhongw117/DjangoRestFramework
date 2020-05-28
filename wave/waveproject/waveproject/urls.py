from django.contrib import admin
from django.urls import path
from uploadreport.views import csv_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('csv-upload/', csv_upload, name="profile_upload"),
]