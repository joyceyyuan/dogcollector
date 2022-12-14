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
    # aka the dog_id
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('dogs/<int:dog_id>/add_walking/', views.add_walking, name='add_walking'),
    # associate a treat with a dog (M:M)
    path('dogs/<int:dog_id>/assoc_treat/<int:treat_id>/', views.assoc_treat, name='assoc_treat'),
    # remove a treat for a dog
    path('dogs/<int:dog_id>/remove_treat/<int:treat_id>/', views.remove_treat, name='remove_treat'),
    path('treats/', views.TreatList.as_view(), name='treats_index'),
    path('treats/<int:pk>/', views.TreatDetail.as_view(), name='treats_detail'),
    path('treats/create/', views.TreatCreate.as_view(), name='treats_create'),
    path('treats/<int:pk>/update/', views.TreatUpdate.as_view(), name='treats_update'),
    path('treats/<int:pk>/delete/', views.TreatDelete.as_view(), name='treats_delete'),
]

