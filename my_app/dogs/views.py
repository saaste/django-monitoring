import json
# from time import sleep
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Dog

@csrf_exempt
def index(request):
    if request.method == "GET":
        # sleep(2)
        dogs = list(Dog.objects.all().values())
        return JsonResponse(dogs, safe=False, json_dumps_params={"ensure_ascii": False})
    
    elif request.method == "POST":
        payload_unicode = request.body.decode('utf-8')
        body = json.loads(payload_unicode)
        
        name = body["name"]
        breed = body["breed"]
        likes_to_bark = body.get("likes_to_bark", False)
        
        new_dog = Dog.objects.create(
            name=name,
            breed=breed,
            likes_to_bark=likes_to_bark
        )
        return JsonResponse(model_to_dict(new_dog), safe=False)

@csrf_exempt
def details(request, id):
    dog = Dog.objects.filter(pk=id).first()
    if not dog:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        return JsonResponse(model_to_dict(dog), safe=False)
    
    elif request.method == "PUT":
        payload_unicode = request.body.decode('utf-8')
        body = json.loads(payload_unicode)
        
        name = body["name"]
        breed = body["breed"]
        likes_to_bark = body.get("likes_to_bark", False)
        
        dog.name = name
        dog.breed = breed
        dog.likes_to_bark = likes_to_bark
        dog.save()
        return JsonResponse(model_to_dict(dog), safe=False)
    
    elif request.method == "DELETE":
        dog.delete()
        return HttpResponse(status=200)
