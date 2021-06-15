from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
   return render(request, 'index.html')

def create_acct(request):
   return render(request, 'create_acct.html')

def signin(request):
   return render(request, 'signin.html')

def register(request):
   errors = User.objects.validator(request.POST)

   if errors:
      for k, v in errors.items():
         messages.error(request, v)
      return redirect('/create')

   else:
      pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
      User.objects.create(
         alias = request.POST['alias'],
         fname = request.POST['fname'],
         lname = request.POST['lname'],
         email = request.POST['email'],
         password = pw_hash
      )
      messages.info(request, 'You have created an account! Please log in.')
   return redirect('/signin')

def authenticate_user(request):
   try:
      user = User.objects.get(email = request.POST['email'])
   except:
      messages.error(request, "Incorrect email address or password.")
      return redirect('/signin')

   if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
      request.session['user_id'] = user.id
      request.session['alias'] = user.alias
      request.session['fname'] = user.fname
      request.session['lname'] = user.lname
      request.session['email'] = user.email
      return redirect('/plantr')

   messages.error(request, "Incorrect email address or password.")
   return redirect('/login')


def logout(request):
   if 'alias' in request.session:
      del request.session['alias']
   if 'user_id' in request.session:
      del request.session['user_id']
   if 'user_fname' in request.session:
      del request.session['fname']
   if 'user_lname' in request.session:
      del request.session['lname']
   if 'user_email' in request.session:
      del request.session['email']
   # request.session.clear()
   return redirect('/')