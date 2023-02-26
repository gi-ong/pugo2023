from . import models
from django.http import HttpResponse


def slug_filter(f):
    def wrap(request, *args, **kwargs):
        w = kwargs.get('slug')
        print('deco:',w)
        try:
            if models.Short.objects.get(short_url=w):
                return f(request, *args, **kwargs)
        except:
            return HttpResponse(status=404)
        
    return wrap
    