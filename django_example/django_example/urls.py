from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^riddles/', include('riddles.urls'), name="riddles"),
    url(r'^admin/', admin.site.urls),
]