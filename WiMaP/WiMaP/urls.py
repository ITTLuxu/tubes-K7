from django.contrib import admin
from django.urls import path
from posting.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= 'index'),
    path('pilih/', pilih, name= 'pilih'),
    path('signup/', signup, name= 'signup')
]
