from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Donate
from .forms import DonateForm


import math


# Create your views here.
def signup_view(request):
    #https://www.youtube.com/watch?v=Xj0MXHrAi9o
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # returns the user to us
            user = form.save()
            # log the user in
            # redirect user to another location
            # return redirect('articles:list')
            login(request, user)
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {'form':form})

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request,user)
            return redirect('http://127.0.0.1:4000/accounts/profile')
    else:
        form = AuthenticationForm()
    return render(request,"accounts/login.html",{'form':form})

def profile_view(request):
    return render(request,"accounts/profile.html",{})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('http://127.0.0.1:4000/accounts/login')

def create_donation(request):
    form = DonateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DonateForm()
    context = {
        'form': form
    }
    return render(request, "accounts/donation_form.html", context)

def deliv_one_view(request):
    form = DonateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DonateForm()
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    donations_costs = Donate.objects.all()
    goal_amount = 0
    current_amount = 0
    for entry in donations_costs:
        if(str(entry.delivery_date) == '2021-01-16'):
            if(entry.user == 'emh'):
                goal_amount = entry.start_cost
            else:
                current_amount += entry.amount
    context = {
        'goal_amount':goal_amount,
        'current_amount': current_amount,
        'form':form
    }
    return render(request, "accounts/delivery_one.html", context)

def deliv_two_view(request):
    form = DonateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DonateForm()
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    donations_costs = Donate.objects.all()
    goal_amount = 0
    current_amount = 0
    for entry in donations_costs:
        if(str(entry.delivery_date) == '2021-01-17'):
            if(entry.user == 'emh'):
                goal_amount = entry.start_cost
            else:
                current_amount += entry.amount
    context = {
        'goal_amount': goal_amount,
        'current_amount': current_amount,
        'form':form,
        'username':username
    }
    return render(request, "accounts/delivery_two.html", context)

def donation_detail_view(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    donations_costs = Donate.objects.all()
    cost_dict = {}
    donation_dict = {}
    delivery_amt = {}
    delivery_cost = {}
    for entry in donations_costs:
        if entry.user == 'emh':
            # if the user is an admin, you add the starting cost to a dictionary
            # {delivery_date: total cost}
            cost_dict[str(entry.delivery_date)] = entry.start_cost
        else:
            # {delivery date: total donations for that day)
            if str(entry.delivery_date) not in donation_dict:
                donation_dict[str(entry.delivery_date)] = entry.amount
            else:
                donation_dict[str(entry.delivery_date)] += entry.amount
    for date, cost in cost_dict.items():
        for date1, amt in donation_dict.items():
            if str(date) == str(date1):
                # maps the {delivery date: total donation amt}
                delivery_amt[str(date)] = float(amt)
                # maps the {delivery date: total goal amt.]}
                delivery_cost[str(date)] = float(cost)

    for date, cost in cost_dict.items():
        if (str(date) not in delivery_amt and str(date) not in delivery_cost):
            delivery_amt[str(date)] = 0.00
            delivery_cost[str(date)] = float(cost)

    context = {
        'amt': delivery_amt,
        'cost': delivery_cost,
        'username':username
    }
    return render(request, "accounts/delivery_dates.html", context)

def user_view(request):
    donations_costs = Donate.objects.all()
    username = None
    total_donated = 0
    total_deliveries = 0
    total_rewards = 0

    if request.user.is_authenticated:
        username = request.user.username
    for person in donations_costs:
        if person.user == username:
            total_donated += person.amount
            total_deliveries += 1
    total_rewards = (total_donated/4)
    total_meals = math.trunc(total_donated)
    hunger_free = math.trunc(total_meals/3)

    context = {
        'username':username,
        'total_donated': total_donated,
        'total_rewards' : total_rewards,
        'total_deliveries': total_deliveries,
        'total_meals':total_meals,
        'hunger_free':hunger_free
    }
    return render(request, "accounts/user_progress.html",context)

"""
user = models.CharField(max_length = 100, default= 'aoc')
    supermarket = models.CharField(max_length = 100)
    delivery_date = models.DateField()

    # starting cost of the delivery
    start_cost = models.DecimalField(max_digits = 100, decimal_places = 2, default = 0.00)

    # amount that the user wants to donate
    amount = models.DecimalField(max_digits = 100, decimal_places = 2)

    # default is that it's true so it's a donation
    cost_type = models.BooleanField(default = True)
"""