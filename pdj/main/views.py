from django.http import Http404, HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect, render
from .forms import FormZap

def index(request):
    return render(request, 'main/index.html')

def page_not_found(request, *args, **kwargs):
    return render(request, 'main/404.html')

def contact(request):
    return render(request, 'main/contact.html')

def category(request, cat_id):
    return index(request)

def register(request):
    if request.method == 'POST':
        form = FormZap(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FormZap()
    return render(request, 'main/register.html', {'form': form})