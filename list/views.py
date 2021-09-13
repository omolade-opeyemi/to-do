from django.shortcuts import render, redirect
from . models import Things
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def homepage(request):
    post = request.user.things_set.all()
    items = Things.objects.all()
    return render(request, 'home.html',{'items':post})

@login_required(login_url="login")
def create(request):
    if request.method == 'POST':
        items = request.POST['content']
        user = request.user
        create = Things.objects.create(todo=items,author=user)

        return redirect('/')
    else:
        return render(request, 'add.html',)

@login_required(login_url="login")
def update(request, pk):
    if request.method == 'POST':
        update = Things.objects.get(id=pk)
        items = request.POST['content']
        update.todo=items
        update.save()
        return redirect('/')

    else:
        item = Things.objects.get(id=pk)
        return render(request, 'update.html', {'item':item})

@login_required(login_url="login")
def delete(request, pk):
    update = Things.objects.get(id=pk).delete()
    return redirect('/')

    