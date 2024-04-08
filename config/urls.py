from django.contrib import admin
from django.urls import path

from reviews.views import ReviewsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ReviewsView.as_view(), name='reviews')
]
