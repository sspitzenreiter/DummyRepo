from django.shortcuts import render
from Captcha_App_1174035.forms import UserForm
# Create your views here.
def index(request):
    return render(request, 'index_035.html')

def users(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
        else:
            print("Form Invalid")
    return render(request, 'daftar_035.html', {'form':form})