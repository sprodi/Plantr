from django.shortcuts import render, redirect
from .models import Plant
from login_app.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView


# Create your views here.
def index(request):
   if 'user_id' not in request.session:
      messages.error(request, "Must be logged in!")
      return redirect('/')
   
   current_user = User.objects.get(id=request.session['user_id'])

   context = {
      'plants': Plant.objects.all(),
      'user': current_user,
      'model': Plant,
   }
   return render(request, 'plantr.html', context)

def addPlant(request):
   if 'user_id' not in request.session:
        messages.error(request, "Must be logged in!")
        return redirect('/')
   else:
      current_user = User.objects.get(id=request.session['user_id'])

      context = {
         "plants": Plant.objects.all(),
         "user": current_user,
      }
      return render(request, 'add_plant.html', context)

def validatePlant(request):
   errors = Plant.objects.plant_validator(request.POST)
   if errors:
      for k, v in errors.items():
         messages.error(request, v)
      return redirect('/plantr/add')
   else:
      Plant.objects.create(
         plantName = request.POST['plantName'],
         plantAlt = request.POST['plantAlt'],
         level = request.POST['level'],
         env = request.POST['env'],
         desc = request.POST['desc'],
         poster = User.objects.get(id=request.session['user_id']),
         plantImg = request.FILES.get('plantImg'),
      )
      return redirect('/plantr')


def updatePlant(request, plant_id):
   errors = Plant.objects.plant_validator(request.POST)
   if errors:
      for k, v in errors.items():
         messages.error(request, v)
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

   else:
      plantToUpdate = Plant.objects.get(id = plant_id)
      plantToUpdate.plantName = request.POST["plantName"]
      plantToUpdate.plantAlt = request.POST["plantAlt"]
      plantToUpdate.level = request.POST["level"]
      plantToUpdate.env = request.POST["env"]
      plantToUpdate.desc = request.POST["desc"]
      plantToUpdate.save()
      return redirect('/plantr')


def delPlant(request, plant_id):
   if 'user_id' not in request.session:
        messages.error(request, "Must be logged in!")
        return redirect('/')

   delPlant = Plant.objects.get(id = plant_id)
   delPlant.delete()
   return HttpResponseRedirect('../')

def viewPlant(request, plant_id):
   if 'user_id' not in request.session:
        messages.error(request, "Must be logged in!")
        return redirect('/')

   current_user = User.objects.get(id=request.session['user_id'])

   context = {
      'plant': Plant.objects.get(id = plant_id),
      'user': current_user,
   }
   return render(request, 'view_plant.html', context)


def editPlant(request, plant_id):
   if 'user_id' not in request.session:
        messages.error(request, "Must be logged in!")
        return redirect('/')
   
   user = User.objects.get(id=request.session['user_id'])
   plantToEdit = Plant.objects.get(id = plant_id)
   context = {
      'user': user,
      'plant': plantToEdit
   }
   return render(request, 'edit_plant.html', context)


def userProfile(request, user_id):
   if 'user_id' not in request.session:
        messages.error(request, "Must be logged in!")
        return redirect('/')
   user = User.objects.get(id = user_id)
   plant = Plant.objects.all()

   current_user = User.objects.get(id=request.session['user_id'])
   cu_posts = Plant.objects.filter(poster=user)

   context = {
      'current_user': current_user,
      'cu_posts': cu_posts,
      'user': user,
      'plant': plant,
   }      
   return render(request, 'user.html', context)

def favPlant(request, plant_id):
   plant = Plant.objects.get(id=plant_id)
   user = User.objects.get(id=request.session['user_id'])
   user.fav_plants.add(plant)
   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def unfavPlant(request, plant_id):
   plant = Plant.objects.get(id=plant_id)
   user = User.objects.get(id=request.session['user_id'])
   user.fav_plants.remove(plant)
   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
