from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout


# register a customer
def register_customer(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.info(request, 'YOUR ACCOUNT HAS BEEN SUCCESSFULLY REGISTERED, PLEASE LOGIN TO CONTINUE')
            return redirect('dashboard')
        else:
            messages.warning(request, 'SOMETHING WENT RONG. PLEASE CHECK FORM INPUTS')
            return redirect('register_customer')
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'user/signup.html', context)


# login a user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print('opssssssssssssssssssssssssssssssssss')
            return redirect('dashboard')
        else:
            messages.warning(request, ' SOMTHING WENT WRONG. PLEASE CHECK THE FORM INPUT')
            print('opppppppppppppppppppppppppppppppppppppp')
            print(username)
            return redirect('login')
    else:
        return render(request, 'user/login.html')
    print('oppsiiiiiiiiiiiiiiiiiiiiiiiiiiiii')


# logout user
def logout_user(request):
    logout(request)
    messages.info(request, 'YOUR LOGOUT NOW. PLEASE LOGIN TO CONTINUE')
    return redirect('login')
