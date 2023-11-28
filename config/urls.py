
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('no-teen', render_no_teen, name="no-teen"),
    path("xyz", xyz_there, name="xyz"),
    path("font-time", render_font_time, name="font-time"),
    path("centered",centered_average, name="average"),
    path('', main_page, name="main"), 
    path('how_old', render_old, name="old"),
    path('order', render_order, name="order"),
    path('functions/hey_you', hey_you_page ,name="hey"),
    path('codingbat', codingbat_page, name="codingbat"),
    path('functions', function_page, name="function"),
    path('admin/', admin.site.urls),
]
