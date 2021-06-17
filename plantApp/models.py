from django.db import models
from login_app.models import User
from django.conf.urls.static import static


class plantsManager(models.Manager):
   def plant_validator(self, postData):
      errors = {}

      if len(postData['plantName']) < 2:
         errors['plantName'] = "Plant name must be at least 2 characters long."
      if len(postData['plantName']) > 255:
         errors['plantName'] = "Plant name must be at less than 50 characters long."
      if len(postData['level']) < 1:
         errors['level'] = "Please choose Care Difficulty"

      if len(postData['env']) < 1:
         errors['env'] = "Please choose type of Envorinment"

      if len(postData['desc']) < 10:
         errors['desc'] = "Instruction must be at least 10 characters long."
      if len(postData['desc']) > 500:
         errors['desc'] = "Instruction must be at less than 500 characters long."
      return errors


class Plant(models.Model):
   LEVELS = (
   (0, ''),
   (1, 'Easy'),
   (2, 'Medium'),
   (3, 'Hard'),
)
   poster = models.ForeignKey(User, related_name = "user_plants", on_delete = models.CASCADE)
   plantName = models.CharField(max_length=50)
   plantAlt = models.CharField(max_length=255, blank=True, default='')
   level = models.CharField(max_length=50)
   env = models.CharField(max_length=1, choices=LEVELS)
   desc = models.CharField(max_length=255)
   plantImg = models.ImageField(upload_to='plants/', null=True, blank=True, default='../static/default_plant.jpg')
   users_fav = models.ManyToManyField(User, related_name = 'fav_plants')
   objects = plantsManager()

   def __str__(self):
      return self.plantName