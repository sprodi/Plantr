from django.db import models
import re

class UserManager(models.Manager):

   def validator(self, post_data):
      errors = {}

      email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

      if len(post_data['alias']) < 2:
         errors['alias'] = 'Username name should be at least two characters long.'

      if len(post_data['fname']) < 2:
         errors['fname'] = 'First name should be at least two characters long.'

      if len(post_data['lname']) < 2:
         errors['lname'] = 'Last name should be at least two characters long.'

      if not email_regex.match(post_data['email']):
         errors['email'] = ("Invalid email address.")

      try:
         self.get(email = post_data['email'])
         errors['email_unique'] = "Email address already in use"
      except:
         pass

      if len(post_data['password']) < 8:
         errors['password'] = 'Password name should be at least two characters long.'
      
      if post_data['password'] != post_data ['confirm_password']:
         errors['password_match'] = 'Passwords should match.'

      return errors



# Create your models here.
class User(models.Model): 
   alias = models.CharField(max_length=50)
   fname = models.CharField(max_length=50)
   lname = models.CharField(max_length=50)
   email = models.CharField(max_length=50)
   password = models.CharField(max_length=50)
   created_at = models.DateTimeField(auto_now_add = True)
   updated_at = models.DateTimeField(auto_now = True)
   objects = UserManager()