from django.shortcuts import render, redirect

from .forms import RegisterForm

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

def register(request):

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/login/')

    return render(request,
                  'register.html',
                  {
                      'form': form
                  })


def user_login(request):

    form = AuthenticationForm()

    if request.method == 'POST':

        form = AuthenticationForm(
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('/')

    return render(request,
                  'login.html',
                  {
                      'form': form
                  })


def user_logout(request):

    logout(request)

    return redirect('/login/')

def admin_login(request):

    form = AuthenticationForm()

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:

            login(request, user)

            return redirect('admin_dashboard')

    return render(request,
                  'admin_login.html',
                  {
                      'form': form
                  })
from django.contrib.admin.views.decorators import staff_member_required

from rooms.models import Room
from bookings.models import Booking
from django.contrib.auth.models import User


@staff_member_required
def admin_dashboard(request):

    total_rooms = Room.objects.count()

    total_bookings = Booking.objects.count()

    total_users = User.objects.count()

    return render(request,
                  'admin_dashboard.html',
                  {
                      'total_rooms': total_rooms,
                      'total_bookings': total_bookings,
                      'total_users': total_users
                  })