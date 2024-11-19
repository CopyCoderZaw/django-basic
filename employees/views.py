from django.shortcuts import render
from employees.models import Employee
# Create your views here.

def index(request):
    employess =Employee.objects.all()
    context = {
        'employess':employess
    }
    return render(request, 'pages/index.html',context)