from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

class LoginView(View):
    def get(self, request):
        return render(request, 'index/Login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('listaAlunos')
            
        return render(request, 'index/Login.html')