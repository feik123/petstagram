from django.urls import path, include

from petstagram.pets import views
from petstagram.pets.views import PetAddPage, PetDetailsPage, PetEditPage, PetDeletePage

urlpatterns = [
    path('add/', PetAddPage.as_view(), name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('delete/', PetDeletePage.as_view(), name='pet-delete'),
        path('', PetDetailsPage.as_view(), name='pet-details'),
        path('edit/', PetEditPage.as_view(), name='pet-edit'),
    ])),

]