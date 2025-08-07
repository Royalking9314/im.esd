# movie_catalogue/urls.py

from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('CATchy.urls')),  # <--- Add this line
]

###   http://127.0.0.1:8000/movie/