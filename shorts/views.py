from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from .models import Short
from . import forms
from . import decorators
import random
import string
from django.contrib import messages



# class IndexCreateView(CreateView):
    # model = Short
    # template_name = "index.html"
    # form_class = forms.ShortForm

@csrf_exempt
def index(request):
    return render(request, 'index.html')
    

@csrf_exempt
def create_shorturl(request):
    if request.method == 'POST':
        try:
            slug = ''.join(random.choice(string.ascii_letters)
                        for x in range(10))
            url = request.POST['url']
            if Short.objects.filter(full_url=url):
                print(Short.objects.filter(full_url=url))
                u = Short.objects.get(full_url=url)
                new_url = u.short_url
                
            else:                
                new_url = Short(full_url=url, short_url=slug)
                new_url.save()
            return JsonResponse({"new_url": new_url, "result": True}, status=200)
        except:
            return JsonResponse({"result": False}, status=200)

        
# @method_decorator(decorators.slug_filter, name="dispatch")
def go_shorturl(request, *args, **kwargs):
    slug = kwargs.get('slug')
    v = Short.objects.get(short_url=slug)
    full_url = v.full_url
    return redirect(full_url)