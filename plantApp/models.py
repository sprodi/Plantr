from django.db import models
from login_app.models import User
from django.conf.urls.static import static


class plantsManager(models.Manager):
   def plant_validator(self, post_data):
      errors = {}

      if len(post_data['plantName']) < 2:
         errors['plantName'] = "Plant name must be at least 2 characters long."
      if len(post_data['plantName']) > 255:
         errors['plantName'] = "Plant name must be at less than 50 characters long."

      if len(post_data['plantAlt']) < 2:
         errors['plantAlt'] = "Environtment name must be at least 2 characters long."
      if len(post_data['plantAlt']) > 255:
         errors['plantAlt'] = "Plant name must be at less than 255 characters long."

      # Figure out how to add radio field for level
      # Figure out how to add drop down field for env

      if len(post_data['desc']) < 2:
         errors['desc'] = "Instruction must be at least 2 characters long."
      if len(post_data['desc']) > 255:
         errors['desc'] = "Instruction must be at less than 255 characters long."

      # if (post_data['plantImg']) < 1:
      #    errors['plantImg'] = "Must upload plant image."

      
      # **** CHANGE THIS TO PLANT CHECK ****
      # TitleCheck = Book.objects.filter(title=post_data['title'])
      # if len(TitleCheck) > 0:
      #    errors['bookExists'] = "Please visit this books page and add the review there"
      # return errors



class Plant(models.Model):
   poster = models.ForeignKey(User, related_name = "user_plants", on_delete = models.CASCADE)
   plantName = models.CharField(max_length=50)
   plantAlt = models.CharField(max_length=255, blank=True, default='')
   level = models.CharField(max_length=50)
   env = models.CharField(max_length=50)
   desc = models.CharField(max_length=255)
   plantImg = models.ImageField(upload_to='plants/', null=True, blank=True, default='../static/default_plant.jpg')
   users_fav = models.ManyToManyField(User, related_name = 'fav_plants')
   objects = plantsManager()

   def __str__(self):
      return self.plantName