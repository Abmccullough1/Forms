
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('logic-2/no-teen-sum/', render_no_teen, name="no-teen"),
    path("string-2/xyz-there/", xyz_there, name="xyz"),
    path("warmup-2/font-times/", render_font_time, name="font-time"),
    path("list-2/centered-average/",centered_average, name="average"),
    path('', main_page, name="main"), 
    path('functions/how_old', render_old, name="old"),
    path('functions/order', render_order, name="order"),
    path('functions/hey_you', hey_you_page ,name="hey"),
    path('codingbat', codingbat_page, name="codingbat"),
    path('functions', function_page, name="function"),
    path('admin/', admin.site.urls),
]
