from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('a',include("accounts.url")),
    path('s', include("Services.url")),
    path('o', include("order.url"))

]
