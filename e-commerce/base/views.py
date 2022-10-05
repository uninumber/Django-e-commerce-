from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from base.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
import os
import stripe



def home(request):
    return render(request, 'home.html')



def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Something went wrong")


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "username or password does not exist.")

 




    context = {}
    return render(request,'login.html', context)
        
       

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')


    return render(request, 'register.html', {'form': form})
    







#STRIP API IMPLEMENTATION
#----------------------
#----------------------

stripe.api_key = 'sk_test_51LhrHvFPj4UkaHNH6r2dgl899NPiyVOMoT18XLLQf5Riuxx52HZoaVdmCvyrqRBXQ1rPv7lRoJoGYJDZsz71LFsA009QVWfqSf'
stripe.Product.list(limit=3)
stripe.Price.list(product='prod_MYboNcGmB4gPIg', active=True)
def headphone(self):
  session = stripe.checkout.Session.create(
    payment_method_types=['card'],

    line_items=[{
        "price": "price_1LpUaRFPj4UkaHNH47uUGVKi", 
        
      
       'adjustable_quantity': {
        'enabled': True,
        'minimum': 1,
        'maximum': 10,
      },
      'quantity': 1,

    }], #quantity

   


        mode='payment',          
        success_url='http://127.0.0.1:8000/successRoom',  
        cancel_url='https://example.com/cancel',          
        )

  subscription = stripe.Subscription.create(
  customer="cus_MQl9voKyImnFs3",
  items=[{'price': 'price_1LhtlcFPj4UkaHNH6zNgCjYh'}],
  coupon='CjfQGhuY',
) #binding coupon to customer and product(discount)

  return redirect(session.url, code=303)



stripe.Price.list(product='prod_MYboNcGmB4gPIg', active=True)
def mouse(self):
  session = stripe.checkout.Session.create(
    payment_method_types=['card'],

    line_items=[{
        "price": "price_1LpUrFFPj4UkaHNHkIvgIkKs", 
        
      
       'adjustable_quantity': {
        'enabled': True,
        'minimum': 1,
        'maximum': 10,
      },
      'quantity': 1,

    }], #quantity

  
        mode='payment',          
        success_url='http://127.0.0.1:8000/successRoom',  
        cancel_url='https://example.com/cancel',          
        )

  subscription = stripe.Subscription.create(
  customer="cus_MQl9voKyImnFs3",
  items=[{'price': 'price_1LhtlcFPj4UkaHNH6zNgCjYh'}],
  coupon='CjfQGhuY',
) #binding coupon to customer and product(discount)

  return redirect(session.url, code=303)









stripe.Price.list(product='prod_MYcGQ9XAiS35ap', active=True)
def micro(self):
  session = stripe.checkout.Session.create(
    payment_method_types=['card'],

    line_items=[{
        "price": "price_1LpV1kFPj4UkaHNHoay3juXK", 
        
      
       'adjustable_quantity': {
        'enabled': True,
        'minimum': 1,
        'maximum': 10,
      },
      'quantity': 1,

    }], #quantity

    discounts=[{
    'coupon': 'IB5EWVQj',
  }],


        mode='payment',          
        success_url='http://127.0.0.1:8000/successRoom',  
        cancel_url='https://example.com/cancel',          
        )

  subscription = stripe.Subscription.create(
  customer="cus_MQl9voKyImnFs3",
  items=[{'price': 'price_1LhtlcFPj4UkaHNH6zNgCjYh'}],
  coupon='CjfQGhuY',
) #binding coupon to customer and product(discount)

  return redirect(session.url, code=303)


def headphoneRoom(request): #sending to productRoom page
    return render(request, 'headphone.html')



def mouseRoom(request):
    return render(request, 'mouse.html')

def microRoom(request):
    return render(request, 'micro.html')


def successRoom(request): #sending you to success page after seccessful purchased
    return render(request, 'success.html')





