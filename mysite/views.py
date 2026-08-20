from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse("<h1> Hello This is my first Django Project</h1>")

def json_test(request):
    return JsonResponse({"name": "amir"})