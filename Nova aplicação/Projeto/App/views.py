from django.shortcuts import render
from App.models import Cursos


# Create your views here.
def index (request):
    # context = {
    #           "cursos": Cursos.objects.all(),
    #           'loginform' :  LoginForm(),
    #          'userform' : UserForm(),
    #        }
    #if request.user.is_authenticated:
    #   context['userform'] = UserForm(instance=User.objects.get(id=request.user.id)) 
    
    return render(request,'index.html')