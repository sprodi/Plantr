from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('add', views.addPlant),
   path('<int:plant_id>/delete', views.delPlant),
   path('<int:plant_id>', views.viewPlant),
   path('users/<int:user_id>', views.userProfile),
   path('<int:plant_id>/fav', views.favPlant),
   path('<int:plant_id>/unfav', views.unfavPlant),

]