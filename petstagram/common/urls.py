from django.urls import path

from petstagram.common import views
from petstagram.common.views import home_page

urlpatterns = [
    path('', home_page, name='home'),
    path('like/<int:photo_id>/', views.likes_functionality, name='like' ),
]