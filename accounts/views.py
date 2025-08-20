from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .powerbi_service import PowerBIService
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard_token.html')

@login_required
@csrf_exempt
def get_powerbi_config(request):
    """API endpoint to get PowerBI embed configuration"""
    try:
        print(f"PowerBI API called by user: {request.user}")
        print(f"User authenticated: {request.user.is_authenticated}")
        
        powerbi_service = PowerBIService()
        config = powerbi_service.get_embed_config()
        
        print(f"PowerBI config result: {config}")
        return JsonResponse(config)
    except Exception as e:
        print(f"PowerBI API error: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

def logout_view(request):
    logout(request)
    return redirect('login')
