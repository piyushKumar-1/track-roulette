from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import EntriesAPIView, updateEntryAPIView, new, index


urlpatterns = [
    path('api/entries/', EntriesAPIView ),
    path('api/entries/<int:id>/<int:num>', updateEntryAPIView ),
    path('api/new', new ),
    url(r'^', index)
]
	