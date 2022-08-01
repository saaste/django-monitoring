import json
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from .models import Cat

@csrf_exempt
def index(request):
    if request.method == "GET":
        cats = list(Cat.objects.all().values())
        return JsonResponse(cats, safe=False, json_dumps_params={"ensure_ascii": False})
    
    elif request.method == "POST":
        payload_unicode = request.body.decode('utf-8')
        body = json.loads(payload_unicode)
        
        name = body["name"]
        breed = body["breed"]
        likes_to_drop_things = body.get("likes_to_drop_things", False)
        is_test = body.get("is_test", False)
        
        new_cat = Cat.objects.create(
            name=name,
            breed=breed,
            likes_to_drop_things=likes_to_drop_things,
            is_test=is_test
        )
        return JsonResponse(model_to_dict(new_cat), safe=False, status=201)

@csrf_exempt
def details(request, id):
    cat = Cat.objects.filter(pk=id).first()
    if not cat:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        return JsonResponse(model_to_dict(cat), safe=False)
    
    elif request.method == "PUT":
        payload_unicode = request.body.decode('utf-8')
        body = json.loads(payload_unicode)
        
        name = body["name"]
        breed = body["breed"]
        likes_to_drop_things = body.get("likes_to_drop_things", False)
        
        cat.name = name
        cat.breed = breed
        cat.likes_to_drop_things = likes_to_drop_things
        cat.save()
        return JsonResponse(model_to_dict(cat), safe=False)

    elif request.method == "DELETE":
        cat.delete()
        return HttpResponse(status=200)

def clean(request):
    Cat.objects.filter(is_test=True).delete()
    return HttpResponse(status=200)