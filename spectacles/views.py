from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

############
# Site Management / User Auth
############

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            pass
    else:
        # Return an 'invalid login' error message.
        pass


def logout_view(request):
    logout(request)
    # Redirect to a success page.

##################
# Base Views
##################

def home(request):
    return HttpResponse("Hello, world!")

@login_required
def geneset_view(request):
    return HttpResponse("Here is a geneset!")