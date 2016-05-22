from django.conf.urls import url, include
from django.contrib import admin

from .router import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^", include(router.urls)),
]
