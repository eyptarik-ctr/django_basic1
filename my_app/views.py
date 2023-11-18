from django.shortcuts import render
from django.http import HttpResponse ,Http404,HttpResponseRedirect

# Create your views here.
def function(request):
    return HttpResponse("There is no DUBA")
animals = {
    "fourLegs":"cat",
    "twoLegs":"chicken",
    "noLegs":"sneak"
    
}
def animal(response,item):
    try:
        animal1 = animals[item]
        return HttpResponse(animal1)
    except:
        raise Http404("this page not found")
    #return HttpResponse(animals.get(item," this page not found"))

def summaration_ex(response , n1,n2):
    return HttpResponse(f"{n1}+{n2} = {n1+n2} ")

def redirectFun(response,s):
    if s == 10:
        return HttpResponseRedirect("/my_app/noLegs")
    elif s == 20:
        return HttpResponseRedirect("/my_app/fourLegs")