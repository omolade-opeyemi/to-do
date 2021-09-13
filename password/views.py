from django.shortcuts import render


# Create your views here.
def Reset(request):
    return render(request, 'index.html')
