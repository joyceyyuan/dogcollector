from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    # route for dogs index
    path('dogs/', views.dogs_index, name='index'),
    #route for the detail page
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    # new route used to show a form and create a dog
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    # pk is what the django views is expecting as a param if we need one, which is short for primary key
    # aka the cat_id
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
]
