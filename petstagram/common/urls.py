from django.urls import path

from petstagram.common import views
from petstagram.common.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),

    path('like/<int:photo_id>/', views.likes_functionality, name='like' ),
    path('share/<int:photo_id>/', views.share_functionality, name='share' ),
    path('comment/<int:photo_id>/', views.comment_functionality, name='comment' ),
]