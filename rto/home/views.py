from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from home.models import Record

def home_page(request):
    if request.method == 'GET':
        return render(request, 'home/index.html',{'records':Record.objects.all()})
    if request.method == 'POST':
        record = get_object_or_404(Record, current=request.POST.get('num'))
        return render(request, 'home/index.html',{'records':Record.objects.all(),'result':record})