from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('list.urls')),
    path('accounts/', include('account.urls')),
    path('password/', include('password.urls')),
]
