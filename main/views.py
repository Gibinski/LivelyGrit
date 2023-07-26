# .\main\views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import VisitorData

def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def statistics(request):
    visitor_data = VisitorData.objects.all()
    return render(request, 'statistics.html', {'visitor_data': visitor_data})
