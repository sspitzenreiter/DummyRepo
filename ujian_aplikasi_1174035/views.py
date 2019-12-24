from django.shortcuts import render
from django.http import HttpResponse
from ujian_aplikasi_1174035.models import User
# Create your views here.

def index(request):
    return render(request, 'ujian_aplikasi_1174035/index_1174035.html')

def User_1174035(request):
    result = User.objects.all()
    datasender = {"daftaruser": result}
    return render(request, 'ujian_aplikasi_1174035/users_1174035.html', datasender)